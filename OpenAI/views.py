from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from softtek_llm.chatbot import Chatbot
from softtek_llm.models import OpenAI
from softtek_llm.cache import Cache
from softtek_llm.vectorStores import PineconeVectorStore
from softtek_llm.embeddings import OpenAIEmbeddings
from softtek_llm.schemas import Filter
import json

OPENAI_API_KEY = "6b25369971534252bbcee5e488ce59f1"
OPENAI_API_BASE = "https://openaistkinno.openai.azure.com/"
OPENAI_EMBEDDINGS_MODEL_NAME = "OpenAIEmbeddings"
OPENAI_CHAT_MODEL_NAME = "InnovationGPT2"
PINECONE_API_KEY = "c77091f2-02df-441f-a09b-a0d1ba6a71a3"
PINECONE_ENVIRONMENT = "gcp-starter"
PINECONE_INDEX_NAME = "default"

vector_store = PineconeVectorStore(
    api_key = PINECONE_API_KEY,
    environment = PINECONE_ENVIRONMENT,
    index_name = PINECONE_INDEX_NAME,
)

embeddings_model = OpenAIEmbeddings(
    api_key = OPENAI_API_KEY,
    model_name = OPENAI_EMBEDDINGS_MODEL_NAME,
    api_type = "azure",
    api_base = OPENAI_API_BASE,
)

cache = Cache(
    vector_store = vector_store,
    embeddings_model = embeddings_model,
)

model = OpenAI(
    api_key = OPENAI_API_KEY,
    model_name = OPENAI_CHAT_MODEL_NAME,
    api_type = "azure",
    api_base = OPENAI_API_BASE,
    verbose = True,
)

filters = [
    Filter(
        type = "DENY",
        case = "YOU JUST GOING TO ANSWER QUESTIONS THAT TALK ABOUT VERBS",
    )
]

chatbot = Chatbot(
    model = model,
    description = "You are a bot lol",
    # filters = filters,
    cache = cache,
    verbose = True,
)

# Create your views here.
@csrf_exempt
def enviar_mensaje(request):
    datos =json.loads(request.body)
    print(datos['mensaje'])
    peticion = datos['mensaje']


    response = chatbot.chat(
        peticion,
    )

    # print(f'Este es el JSON del back: {response.message.content}')

    diccionario = {
        'mensaje': f'{response.message.content}'
    }
    
    return HttpResponse(json.dumps(diccionario))