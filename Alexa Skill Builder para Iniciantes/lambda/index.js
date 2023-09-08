// This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK (v2).
// Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
// session persistence, api calls, and more.
const Alexa = require('ask-sdk-core');

const persistenceAdapter = require('ask-sdk-s3-persistence-adapter');

const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest';
    },
    async handle(handlerInput) {
        
        const FULL_NAME_PERMISSION = "alexa::profile:name:read";
        const EMAIL_PERMISSION = "alexa::profile:email:read";
        
        const { serviceClientFactory } = handlerInput;
        
        try {
            
            const upsServiceClient = serviceClientFactory.getUpsServiceClient();
            
            const profileName  = await upsServiceClient.getProfileName();
            const profileEmail = await upsServiceClient.getProfileEmail();
            
            console.log("[EMAIL]====> ",profileEmail);
            
            const speakOutput = 'Oi bem vindo ao ingressos populares, ' +profileName+ ',podemos fazer uma reserva para você, ou consultar uma reserva existente. O que você deseja ?';
            return handlerInput.responseBuilder
                .speak(speakOutput)
                .reprompt(speakOutput)
                .getResponse();
     
            
        } catch (error) {
            if ( error.statusCode === 403 ){
                const speakOutput = "Olá, você precisa habilitar as permissões necessárias para melhor experiência  da nossa  skill";
                return handlerInput.responseBuilder
                    .speak(speakOutput)
                    .withAskForPermissionsConsentCard([FULL_NAME_PERMISSION,EMAIL_PERMISSION])
                    .getResponse();
            } else {
                console.log(error.name);
                const speakOutput = "oops,  aconteceu um erro"
                 return handlerInput.responseBuilder
                    .speak(speakOutput)
                    .getResponse();
            }
        }
        
    }
};

const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Hello World!';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const ConsultarReservaIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'ConsultarReservaIntent';
    },
    async handle(handlerInput) {
        
        const attributesManager = handlerInput.attributesManager;
        
        //const ingressosAttributes = attributesManager.getSessionAttributes();
        
        const ingressosAttributes = await attributesManager.getPersistentAttributes();
        
        let speakOutput;
        
        let qtde = parseInt(ingressosAttributes.qtde);
        
        if (qtde > 0){
            speakOutput = 'Você tem uma reserva de '+ingressosAttributes.qtde+' ingresso(s) para o dia '+ingressosAttributes.data+' as '+ingressosAttributes.hora;
        } else {
            speakOutput = 'Não tem nenhuma reserva no momento';
        }
      
        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('O que mais podemos fazer por voce ?')
            .withShouldEndSession(true)
            .getResponse();
    }
};


const ReservarIngressoIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'ReservarIngressoIntent';
    },
    async handle(handlerInput) {
        
        console.log('[filme]',Alexa.getSlotValue(handlerInput.requestEnvelope,'nomeFilme'));
        console.log('[data]',Alexa.getSlotValue(handlerInput.requestEnvelope,'dataSessao'));
        console.log('[hora]',Alexa.getSlotValue(handlerInput.requestEnvelope,'horaSessao'));
        console.log('[qtde]',Alexa.getSlotValue(handlerInput.requestEnvelope,'qtdeIngressos'));
        console.log('[setor]',Alexa.getSlotValue(handlerInput.requestEnvelope,'setorCinema'));
        
        const attributesManager = handlerInput.attributesManager;
        
        const ingressosAttributes = {
            "nome":Alexa.getSlotValue(handlerInput.requestEnvelope,'nomeFilme'),
            "data":Alexa.getSlotValue(handlerInput.requestEnvelope,'dataSessao'),
            "hora":Alexa.getSlotValue(handlerInput.requestEnvelope,'horaSessao'),
            "qtde":Alexa.getSlotValue(handlerInput.requestEnvelope,'qtdeIngressos'),
            "setor":Alexa.getSlotValue(handlerInput.requestEnvelope,'setorCinema')
        }
        
        attributesManager.setSessionAttributes(ingressosAttributes);
        
        attributesManager.setPersistentAttributes(ingressosAttributes);
        await attributesManager.savePersistentAttributes();
        
        const ingresso = "Seu filme: "+ingressosAttributes.nome+" - foi reservado";
        
        const speakOutput = 'Seu ingresso foi reservado';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.withSimpleCard("Reserva de Ingresso", ingresso )
            .withStandardCard("Reservar de Ingresso", ingresso, "https://universidadeglobal.com.br/alexa/icone.png", "https://universidadeglobal.com.br/alexa/icone.png")
            .getResponse();
    }
};


const FallBackIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.FallbackIntent';
    },
    handle(handlerInput) {
        const speakOutput = ' Humm, não entendi, você pode reservar ingressos aqui na nossa skill ';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};


const HelpIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'é fácil fazer uma reserva, basta dizer reservar ingresso ';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};
const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && (Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.CancelIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.StopIntent');
    },
    handle(handlerInput) {
        const speakOutput = 'Tudo bem, vou embora';
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .getResponse();
    }
};
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};

// The intent reflector is used for interaction model testing and debugging.
// It will simply repeat the intent the user said. You can create custom handlers
// for your intents by defining them above, then also adding them to the request
// handler chain below.
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speakOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

// Generic error handling to capture any syntax or routing errors. If you receive an error
// stating the request handler chain is not found, you have not implemented a handler for
// the intent being invoked or included it in the skill builder below.
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.log(`~~~~ Error handled: ${error.stack}`);
        const speakOutput = `Sorry, I had trouble doing what you asked. Please try again.`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

// The SkillBuilder acts as the entry point for your skill, routing all request and response
// payloads to the handlers above. Make sure any new handlers or interceptors you've
// defined are included below. The order matters - they're processed top to bottom.
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        HelloWorldIntentHandler,
        ConsultarReservaIntentHandler,
        ReservarIngressoIntentHandler,
        FallBackIntentHandler,
        HelpIntentHandler,
        CancelAndStopIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler, // make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
    )
    .addErrorHandlers(
        ErrorHandler,
    )
    .withPersistenceAdapter(
        new persistenceAdapter.S3PersistenceAdapter({bucketName: process.env.S3_PERSISTENCE_BUCKET})
    )
    .withApiClient( 
        new Alexa.DefaultApiClient()
    )
    .lambda();
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
