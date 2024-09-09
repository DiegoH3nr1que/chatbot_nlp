import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet as wn
from difflib import get_close_matches

# Baixar os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Texto que conta a história de João
text = """
João é um jovem aventureiro que vive em Recife. Desde pequeno, ele sempre sonhou em explorar a natureza e viver em contato com o meio ambiente. Recentemente, João decidiu realizar seu sonho de se tornar um guia de ecoturismo. Ele passou os últimos anos estudando biologia e técnicas de sobrevivência para garantir que pudesse oferecer uma experiência segura e educativa para os turistas. 
João é apaixonado por trilhas e frequentemente organiza expedições em reservas naturais, onde os visitantes podem observar a rica biodiversidade da região. Em seus dias de folga, ele gosta de praticar fotografia de vida selvagem e tem um blog onde compartilha suas aventuras e dicas para quem deseja se aventurar pela natureza. 
Além de seu trabalho, João também é dedicado à conservação ambiental e participa de projetos locais para proteger a fauna e flora de sua região. Nos fins de semana, ele frequentemente participa de mutirões para limpar trilhas e promover a educação ambiental nas comunidades locais.
"""

# Tokenizar o texto em sentenças para facilitar a busca de respostas
sentences = sent_tokenize(text)

# Função para encontrar sinônimos em português
def get_synonyms(word):
    synonyms = set(lemma.name() for syn in wn.synsets(word, lang='por') for lemma in syn.lemmas('por'))
    return synonyms

# Função de similaridade semântica e correspondência de palavras próximas
def semantic_similarity(user_input, keywords):
    user_words = word_tokenize(user_input)
    for word in user_words:
        # Verificar correspondências aproximadas e sinônimos
        close_matches = get_close_matches(word, keywords, n=1, cutoff=0.7)
        if close_matches:
            return True
        synonyms = get_synonyms(word)
        if any(get_close_matches(syn, keywords, n=1, cutoff=0.7) for syn in synonyms):
            return True
    return False

# Função para encontrar uma resposta mais detalhada no texto
def find_detailed_answer(user_input):
    user_tokens = word_tokenize(user_input)
    best_match = None
    best_score = 0
    
    # Procurar uma sentença que tenha mais similaridade com o input do usuário
    for sentence in sentences:
        sentence_tokens = word_tokenize(sentence.lower())
        common_words = set(user_tokens).intersection(sentence_tokens)
        match_score = len(common_words) / len(user_tokens)
        
        if match_score > best_score:
            best_score = match_score
            best_match = sentence
    
    # Retorna a melhor sentença encontrada, ou None se não houver uma boa correspondência
    return best_match if best_score > 0.3 else None

# Função para mapear perguntas a respostas com base na história de João
def answer_question(user_input):
    # Procurar uma resposta mais precisa na história de João
    detailed_answer = find_detailed_answer(user_input)
    
    if detailed_answer:
        return f"{detailed_answer}"
    
    # Se não encontrar uma resposta exata, gerar uma resposta genérica
    return "Desculpe, não encontrei uma resposta exata. Pergunte sobre as aventuras de João, ecoturismo ou sua vida em Recife."

# Função do chatbot aprimorado
def chatbot():
    print("Olá! Eu sou o chatbot. Pergunte-me sobre João e eu tentarei responder com base na história dele.")
    
    while True:
        user_input = input("Você: ").strip().lower()
        if user_input in ['sair', 'exit', 'quit']:
            print("Chatbot: Até mais!")
            break
        
        response = answer_question(user_input)
        print(f"Chatbot: {response}")

# Iniciar o chatbot
chatbot()
