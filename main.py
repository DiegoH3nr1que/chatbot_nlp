import nltk
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from difflib import get_close_matches

# Baixar os recursos necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Texto que conta a história de alguém
text = """
João é um jovem aventureiro que vive em Recife. Desde pequeno, ele sempre sonhou em explorar a natureza e viver em contato com o meio ambiente. Recentemente, João decidiu realizar seu sonho de se tornar um guia de ecoturismo. Ele passou os últimos anos estudando biologia e técnicas de sobrevivência para garantir que pudesse oferecer uma experiência segura e educativa para os turistas. 

João é apaixonado por trilhas e frequentemente organiza expedições em reservas naturais, onde os visitantes podem observar a rica biodiversidade da região. Em seus dias de folga, ele gosta de praticar fotografia de vida selvagem e tem um blog onde compartilha suas aventuras e dicas para quem deseja se aventurar pela natureza. 

Além de seu trabalho, João também é dedicado à conservação ambiental e participa de projetos locais para proteger a fauna e flora de sua região. Nos fins de semana, ele frequentemente participa de mutirões para limpar trilhas e promover a educação ambiental nas comunidades locais.
"""


# Função para encontrar sinônimos em português
def get_synonyms(word):
    synonyms = set(lemma.name() for syn in wn.synsets(word, lang='por') for lemma in syn.lemmas('por'))
    return synonyms

# Função de similaridade semântica e correspondência de palavras próximas
def semantic_similarity(user_input, keywords):
    user_words = word_tokenize(user_input)
    for word in user_words:
        # Verificar correspondências aproximadas e sinônimos
        close_matches = get_close_matches(word, keywords, n=1, cutoff=0.8)
        if close_matches:
            return True
        synonyms = get_synonyms(word)
        if any(get_close_matches(syn, keywords, n=1, cutoff=0.8) for syn in synonyms):
            return True
    return False

def analyze_sentiment(text):
    blob = TextBlob(text)
    # Retornar sentimento (positivo, negativo ou neutro)
    if blob.sentiment.polarity > 0:
        return 'positivo'
    elif blob.sentiment.polarity < 0:
        return 'negativo'
    else:
        return 'neutro'

# Função do chatbot aprimorado
def chatbot():
    print("Olá! Eu sou o chatbot. Pergunte-me sobre João e eu tentarei responder com base na história dele.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break

        sentiment = analyze_sentiment(user_input)
        
        if sentiment == 'positivo':
            response = "Que ótimo ouvir isso! Estou aqui para ajudar. Pergunte-me sobre João e eu farei o meu melhor para responder."
        elif sentiment == 'negativo':
            response = "Sinto muito que você esteja se sentindo assim. Vou tentar ajudar com sua pergunta sobre João."
        else:
            response = "Entendi. Vou responder com base na história de João."

        if 'guias de ecoturismo' in user_input or semantic_similarity(user_input, ['ecoturismo', 'guia', 'turismo']):
            response = "João decidiu se tornar um guia de ecoturismo após estudar biologia e técnicas de sobrevivência para oferecer uma experiência educativa e segura para os turistas."
        elif 'recife' in user_input or semantic_similarity(user_input, ['recife', 'cidade', 'moradia']):
            response = "João vive em Recife e é apaixonado por explorar a natureza ao seu redor."
        elif 'trilhas' in user_input or semantic_similarity(user_input, ['trilhas', 'reservas naturais', 'expedições']):
            response = "João organiza expedições em reservas naturais e trilhas para que os visitantes possam observar a biodiversidade local."
        elif 'fotografia' in user_input or semantic_similarity(user_input, ['fotografia', 'blog']):
            response = "João gosta de fotografia de vida selvagem e mantém um blog onde compartilha suas aventuras e dicas para aventureiros."
        elif 'conservação ambiental' in user_input or semantic_similarity(user_input, ['conservação', 'ambiental', 'proteção']):
            response = "João participa de projetos de conservação ambiental para proteger a fauna e a flora da região."
        elif 'voluntariado' in user_input or semantic_similarity(user_input, ['voluntariado', 'ajuda', 'comunidade']):
            response = "João também participa de projetos de voluntariado para ajudar a comunidade local."
        elif 'futuro' in user_input or semantic_similarity(user_input, ['futuro', 'sonhos', 'planos']):
            response = "No futuro, João sonha em expandir seu trabalho como guia de ecoturismo e explorar ainda mais a biodiversidade do Brasil."
        elif 'natureza' in user_input or semantic_similarity(user_input, ['natureza', 'ambiental', 'ecologia']):
            response = "João aprecia a natureza e gosta de fazer trilhas em parques naturais para se conectar com o meio ambiente."
        elif 'recife' in user_input or semantic_similarity(user_input, ['recife', 'cidade']):
            response = "João vive em Recife, uma cidade vibrante com uma rica biodiversidade ao seu redor."
        elif 'expedições' in user_input or semantic_similarity(user_input, ['expedições', 'aventuras']):
            response = "João organiza expedições para que as pessoas possam explorar a natureza e aprender mais sobre o meio ambiente."
        elif 'biologia' in user_input or semantic_similarity(user_input, ['biologia', 'estudos', 'científico']):
            response = "João estudou biologia para se preparar para seu trabalho como guia de ecoturismo."
        elif 'vacation' in user_input or semantic_similarity(user_input, ['vacation', 'holiday']):
            response = "João utiliza suas férias para viajar e explorar novos destinos."
        elif 'hobbies' in user_input or semantic_similarity(user_input, ['hobbies', 'passatempos']):
            response = "Além de guiar expedições, João gosta de fotografia e de escrever sobre suas aventuras em seu blog."
        elif 'voluntariado' in user_input or semantic_similarity(user_input, ['voluntariado', 'ajuda', 'comunidade']):
            response = "João dedica tempo ao voluntariado, ajudando em causas sociais e ambientais."
        else:
            response = "Desculpe, não entendi sua pergunta. Pode perguntar sobre a história de João, suas atividades ou onde ele vive?"

        print(f"Chatbot: {response}")

# Iniciar o chatbot
chatbot()