var dialaudio = new Audio('dial.mp3');
var inputCount = 0;

var simpleInput = "";
var userId = "";
var bingClientTTS = new BingTTS.Client("4a346adfa3564855b070261ae4a99d0c");

var bingClientSTT = Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClientWithIntent(
                        "de-DE",
                        "4a346adfa3564855b070261ae4a99d0c",
                        "a72e1a7f-3177-49e1-bd7a-63c6134673f8",
                        "2037ad0154d14287b2d96a58d5a77f16");

var bingClientSimpleSTT = Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClient(
    Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionMode.shortPhrase,
    "de-DE",
    "4a346adfa3564855b070261ae4a99d0c");

bingClientSTT.onFinalResponseReceived = function (response) {
    setText(JSON.stringify(response));
}

bingClientSTT.onIntentReceived = function (response) {
    setText(response);
    intentInput(JSON.parse(response));
};

bingClientSimpleSTT.onFinalResponseReceived = function (response) {
    setText(JSON.stringify(response));
    employeeNumberInput(response);
}

function intentInput(response) {
    if (response != undefined && response.intents.length > 0) {
        if (response.intents[0].intent == "Confirm" && parseFloat(response.intents[0].score) > 0.5) {
            // YES!!! We have a confirmed employee number
            bingClientTTS.synthesize("Die Mitarbeiter und Ihre Stimme wurde erfolgreich bestätigt, was kann ich für Sie tun?", BingTTS.SupportedLocales.deDE_Female, () => {
                bingClientSTT.startMicAndRecognition();
                setTimeout(function () {
                    bingClientSTT.endMicAndRecognition();
                }, 7000);             
            });               
        }
        else if (response.intents[0].intent == "Deny" && parseFloat(response.intents[0].score) > 0.5) {
            // Employee ID not confirmed, retry
            startSupport();               
        }        
        else if (response.intents[0].intent == "ResetPassword" && parseFloat(response.intents[0].score) > 0.5) {
            // User wants to reset password
            bingClientTTS.synthesize("Ihr Passwort muss neu gesetzt werden.  Um ihre Identität zu verifizieren ist ein Sicherheitscode an ihr Mobiltelefon geschickt worden. Bitte sagen sie die Buchstaben des Codes und drucken sie danach die # Taste.", BingTTS.SupportedLocales.deDE_Female, () => {
                inputCount = 0;
                bingClientSimpleSTT.startMicAndRecognition();
                setTimeout(function () {
                    bingClientSimpleSTT.endMicAndRecognition();
                }, 7000);             
            });               
        }
        else {
            bingClientTTS.synthesize("Leider komme ich nicht weiter, Ich leite Sie jetzt weiter an einen Servicemitarbeiter. Auf wieder hören!", BingTTS.SupportedLocales.deDE_Female, () => {
                //startSupport();
                init();
            });                  
        }
    }
}

function employeeNumberInput(response) {
   
    inputCount++;
    if (response != undefined && response.length > 0 && userId == "") {
        userId = response[0].display;

        bingClientTTS.synthesize("Ich habe die Nummer " + response[0].lexical + " verstanden, ist das richtig?", BingTTS.SupportedLocales.deDE_Female, () => {
            bingClientSTT.startMicAndRecognition();
            setTimeout(function () {
                bingClientSTT.endMicAndRecognition();
            }, 3000);             
        });                 
    }
    else if (response != undefined && response.length > 0) {
        // User Id is already entered, so this must be the code

        bingClientTTS.synthesize("Das Sicherheitscode " + response[0].lexical + " ist richtig, bitte melden Sie sich erneut an um ein neues Passwort zu setzen. Vielen Dank, auf wieder hören!", BingTTS.SupportedLocales.deDE_Female, () => {
            // FINISHED
            init();
        });                 
    }    
    else if (inputCount > 2) {
        bingClientTTS.synthesize("Leider komme ich nicht weiter, Ich leite Sie jetzt weiter an einen Servicemitarbeiter. Auf wieder hören!", BingTTS.SupportedLocales.deDE_Female, () => {
            init();
        });         
    }
    else {
        bingClientTTS.synthesize("Ich habe das leider nicht verstanden. Bitte sagen sie klar und deutlich Ihre Mitarbeiter Nummer und drucken Sie danach die # Taste.", BingTTS.SupportedLocales.deDE_Female, () => {
            bingClientSimpleSTT.startMicAndRecognition();
            setTimeout(function () {
                bingClientSimpleSTT.endMicAndRecognition();
            }, 15000); 
        }); 
    }
}

function setText(newText) {
   document.getElementById("output").value += newText; 
}

function init() {
    inputCount = 0;
    simpleInput = "";
    userId = "";
}

function fivepress() {

    inputCount++;

    if (inputCount <= 4) {
       dialaudio.play();
    }

    if (inputCount >= 4) {
        startSupport();
    }
}

function startSupport() {
    init();
    bingClientTTS.multipleXHR = false; 
    bingClientTTS.synthesize("Herzlich willkommen beim Mitarbeitersupport. Bitte sprechen sie Ihre Mitarbeiter Nummer klar und deutlich aus.", BingTTS.SupportedLocales.deDE_Female, () => {
        bingClientSimpleSTT.startMicAndRecognition();
        setTimeout(function () {
            bingClientSimpleSTT.endMicAndRecognition();
        }, 7000); 
    });  
}

function inputfinished() {
    //bingClientSimpleSTT.endMicAndRecognition();
}

//# sourceMappingURL=index.js.map