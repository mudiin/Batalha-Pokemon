import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# Biblioteca responsável por conversar com o seu SO (Sistema Operacional)
import os
import random
import copy

# ==============================================================================
# BASE DE DADOS DO JOGO (Extraída diretamente do seu Planeamento)
# ==============================================================================
DADOS_POKEMON = {
    "Greninja": {
        "tipos": ["Água", "Sombrio"], "hp": 110, "ataque": 95, "ataque_especial":103, "defesa": 67, "defesa_especial":71, "velocidade": 122,
        "movimentos": {"Shuriken de água": {"categoria":"Especial", "tipo": "Água"}, "Pulso Sombrio": {"categoria": "Especial", "tipo": "Sombrio"}},
        "enfase": "Comprimindo a água, ele cria shurikens afiadas que podem cortar até mesmo o metal."
    },
    "Venusaur": {
        "tipos": ["Planta", "Veneno"], "hp": 120, "ataque": 82, "ataque_especial": 100, "defesa": 83, "defesa_especial": 100, "velocidade": 80,
        "movimentos": {"Chicote de cipó": {"tipo": "Planta", "categoria": "Físico"}, "Bomba de Lodo": {"tipo": "Veneno", "categoria": "Especial"}},
        "enfase": "A flor nas suas costas cresce absorvendo luz solar. Ela exala um aroma reconfortante."
    },
    "Blaziken": {
        "tipos": ["Fogo", "Lutador"], "hp": 115, "ataque": 120, "ataque_especial": 110, "defesa": 70, "defesa_especial": 70, "velocidade": 80,
        "movimentos": {"Chute Labareda": {"categoria": "Físico", "tipo": "Fogo"}, "Gancho Alto": {"categoria": "Físico", "tipo": "Lutador"}},
        "enfase": "Chamas Amarelas brotam dos seus pulsos quando ele enfrenta um oponente corajoso."
    },
    "Lucario": {
        "tipos": ["Lutador", "Aço"], "hp": 110, "ataque": 110, "ataque_especial": 115, "defesa": 70, "defesa_especial": 70, "velocidade": 90,
        "movimentos": {"Esfera de Aura": {"categoria": "Especial", "tipo": "Lutador"}, "Garra de Metal": {"categoria": "Físico", "tipo": "Aço"}},
        "enfase": "Ao ler a aura dos seus adversários, ele consegue prever os seus movimentos antes mesmo que aconteçam."
    },
    "Gengar": {
        "tipos": ["Fantasma", "Veneno"], "hp": 105, "ataque": 65, "ataque_especial": 130, "defesa": 60, "defesa_especial": 75, "velocidade": 110,
        "movimentos": {"Bola Sombria": {"categoria": "Especial", "tipo": "Fantasma"}, "Toxina": {"categoria": "Especial", "tipo": "Veneno"}},
        "enfase": "Esconde-se nas sombras das pessoas à noite para absorver o calor do corpo delas."
    },
    "Snorlax": {
        "tipos": ["Normal"], "hp": 160, "ataque": 110, "ataque_especial": 65, "defesa": 65, "defesa_especial": 110, "velocidade": 30,
        "movimentos": {"Giga Impacto":{"categoria": "Físico", "tipo": "Normal"}, "Soco de Gelo": {"categoria": "Físico", "tipo": "Gelo"}},
        "enfase": "Não fica satisfeito a menos que coma 400 quilos de comida todos os dias. Depois, vai dormir."
    },
    "Alakazam": {
        "tipos": ["Psíquico"], "hp": 100, "ataque": 50, "ataque_especial": 135, "defesa": 45, "defesa_especial": 95, "velocidade": 120,
        "movimentos": {"Confusão": {"categoria": "Especial", "tipo": "Psíquico"}, "Clarão Ofuscante": {"categoria": "Especial", "tipo": "Fada"}},
        "enfase": "O seu cérebro nunca para de crescer, fazendo com que o seu quociente de inteligência ultrapasse os 5.000."
    },
    "Umbreon": {
        "tipos": ["Sombrio"], "hp": 135, "ataque": 65, "ataque_especial": 60, "defesa": 110, "defesa_especial": 130, "velocidade": 65,
        "movimentos": {"Jogo Sujo": {"categoria": "Físico", "tipo": "Sombrio"}, "Ataque Rápido": {"categoria": "Físico", "tipo": "Normal"}},
        "enfase": "Quando exposto à luz da lua, os anéis no seu corpo brilham levemente, intimidando os inimigos."
    },
    "Jolteon": {
        "tipos": ["Elétrico"], "hp": 105, "ataque": 65, "ataque_especial": 110, "defesa": 60, "defesa_especial": 95, "velocidade": 130,
        "movimentos": {"Raio de Trovão": {"categoria": "Especial", "tipo": "Elétrico"}, "Sinalizador": {"categoria":"Especial", "tipo": "Inseto"}},
        "enfase": "Acumula iões negativos na atmosfera para lançar relâmpagos que chegam a 10.000 volts."
    },
    "Mamoswine": {
        "tipos": ["Gelo", "Terrestre"], "hp": 145, "ataque": 130, "ataque_especial": 70, "defesa": 80, "defesa_especial": 60, "velocidade": 80,
        "movimentos": {"Estalactite": {"categoria": "Físico", "tipo": "Gelo"}, "Tiro de Lama": {"categoria": "Físico", "tipo": "Terrestre"}},
        "enfase": "Um Pokémon que prosperou na Era do Gelo. As suas presas impressionantes são feitas de puro gelo."
    }
}
 # Pokémons dos treinadores (Balanceados e Corrigidos)

DADOS_POKEMON_TREINADORES = {
    "Charizard": {
        "tipos": ["Fogo", "Voador"], "hp": 115, "ataque": 84, "ataque_especial": 109, "defesa": 78, "defesa_especial": 85, "velocidade": 100,
        "movimentos": {
            "Lança-Chamas": {"categoria": "Especial", "tipo": "Fogo"}, 
            "Ataque de Asa": {"categoria": "Físico", "tipo": "Voador"}, 
            "Pulso Dragão": {"categoria": "Especial", "tipo": "Dragão"}
        },
        "enfase": "Cospe chamas quentes o suficiente para derreter rochas. Pode causar incêndios florestais soprando fogo."
    },
    "Garchomp": {
        "tipos": ["Dragão", "Terrestre"], "hp": 128, "ataque": 130, "ataque_especial": 80, "defesa": 95, "defesa_especial": 95, "velocidade": 102,
        "movimentos": {
            "Terremoto": {"categoria": "Físico", "tipo": "Terrestre"}, 
            "Garra_Dragão": {"categoria": "Físico", "tipo": "Dragão"}, 
            "Gume de Pedra": {"categoria": "Físico", "tipo": "Pedra"}
        },
        "enfase": "Quando dobra o corpo e estende as asas, parece um caça a jato. Consegue voar em velocidade sônica."
    },
    "Metagross": {
        "tipos": ["Aço", "Psíquico"], "hp": 120, "ataque": 135, "ataque_especial": 95, "defesa": 130, "defesa_especial": 90, "velocidade": 70,
        "movimentos": {
            "Punho Meteoro": {"categoria": "Físico", "tipo": "Aço"}, 
            "Confusão": {"categoria": "Especial", "tipo": "Psíquico"}, 
            "Deslizamento de Rocha": {"categoria": "Físico", "tipo": "Pedra"}
        },
        "enfase": "Possui quatro cérebros combinados que formam uma rede neural complexa, superando um supercomputador."
    },
    "Dragonite": {
        "tipos": ["Dragão", "Voador"], "hp": 131, "ataque": 134, "ataque_especial": 100, "defesa": 95, "defesa_especial": 100, "velocidade": 80,
        "movimentos": {
            "Ultraje": {"categoria": "Físico", "tipo": "Dragão"}, 
            "Hiper Raio": {"categoria": "Especial", "tipo": "Normal"}, 
            "Soco do Trovão": {"categoria": "Físico", "tipo": "Elétrico"}
        },
        "enfase": "Um Pokémon marinho extremamente calmo e bondoso, mas que destrói tudo ao seu redor se ficar furioso."
    },
    "Gardevoir": {
        "tipos": ["Psíquico", "Fada"], "hp": 108, "ataque": 65, "ataque_especial": 125, "defesa": 65, "defesa_especial": 115, "velocidade": 80,
        "movimentos": {
            "Clarão Ofuscante": {"categoria": "Especial", "tipo": "Fada"}, 
            "Psíquico": {"categoria": "Especial", "tipo": "Psíquico"}, 
            "Bola Sombria": {"categoria": "Especial", "tipo": "Fantasma"}
        },
        "enfase": "Capaz de prever o futuro. Tem o poder psicocinético de distorcer as dimensões e criar um pequeno buraco negro."
    },
    "Tyranitar": {
        "tipos": ["Pedra", "Sombrio"], "hp": 140, "ataque": 134, "ataque_especial": 95, "defesa": 110, "defesa_especial": 100, "velocidade": 61,
        "movimentos": {
            "Mastigar": {"categoria": "Físico", "tipo": "Sombrio"}, 
            "Desabamento": {"categoria": "Físico", "tipo": "Pedra"}, 
            "Soco de Fogo": {"categoria": "Físico", "tipo": "Fogo"}
        },
        "enfase": "Sua carcaça é blindada e insolente contra quase qualquer impacto. Costuma derrubar montanhas inteiras para fazer seu ninho."
    },
    "Lapras": {
        "tipos": ["Água", "Gelo"], "hp": 165, "ataque": 85, "ataque_especial": 85, "defesa": 80, "defesa_especial": 95, "velocidade": 60,
        "movimentos": {
            "Raio Congelante": {"categoria": "Especial", "tipo": "Gelo"},
            "Surfar": {"categoria": "Especial", "tipo": "Água"},
            "Golpe de Corpo": {"categoria": "Físico", "tipo": "Normal"}
        },
        "enfase": "Um Pokémon de alta inteligência que adora ler a mente das pessoas e navegar cantando pelos oceanos gélidos."
    },
    "Pikachu": {
        "tipos": ["Elétrico"], "hp": 95, "ataque": 110, "ataque_especial": 105, "defesa": 60, "defesa_especial": 70, "velocidade": 135,
        "movimentos": {
            "Choque do Trovão": {"categoria": "Especial", "tipo": "Elétrico"},
            "Cauda de Ferro": {"categoria": "Físico", "tipo": "Aço"},
            "Ataque Rápido": {"categoria": "Físico", "tipo": "Normal"}
        },
        "enfase": "Acumula eletricidade estática nas bolsas de suas bochechas. Quando libera energia, pode gerar relâmpagos violentos."
    }
}

TABELA_TIPAGENS = {
    "Fogo": {
        "vantagens": ["Planta", "Gelo", "Aço"],
        "desvantagens": ["Fogo", "Água", "Pedra", "Dragão"],
        "imunidades": []
    },
    "Água": {
        "vantagens": ["Fogo", "Terrestre", "Pedra"],
        "desvantagens": ["Água", "Planta", "Dragão"],
        "imunidades": []
    },
    "Planta": {
        "vantagens": ["Água", "Terrestre", "Pedra"],
        "desvantagens": ["Fogo", "Planta", "Veneno", "Voador", "Aço", "Dragão"],
        "imunidades": []
    },
    "Elétrico": {
        "vantagens": ["Água", "Voador"],
        "desvantagens": ["Elétrico", "Planta", "Dragão"],
        "imunidades": ["Terrestre"]
    },
    "Gelo": {
        "vantagens": ["Planta", "Terrestre", "Voador", "Dragão"],
        "desvantagens": ["Fogo", "Água", "Gelo", "Aço"],
        "imunidades": []
    },
    "Lutador": {
        "vantagens": ["Normal", "Gelo", "Pedra", "Sombrio", "Aço"],
        "desvantagens": ["Veneno", "Voador", "Psíquico", "Inseto", "Fada"],
        "imunidades": ["Fantasma"]
    },
    "Veneno": {
        "vantagens": ["Planta", "Fada"],
        "desvantagens": ["Veneno", "Terrestre", "Pedra", "Fantasma"],
        "imunidades": ["Aço"]
    },
    "Terrestre": {
        "vantagens": ["Fogo", "Elétrico", "Veneno", "Pedra", "Aço"],
        "desvantagens": ["Planta", "Inseto"],
        "imunidades": ["Voador"]
    },
    "Voador": {
        "vantagens": ["Planta", "Lutador", "Inseto"],
        "desvantagens": ["Elétrico", "Aço", "Pedra"],
        "imunidades": []
    },
    "Psíquico": {
        "vantagens": ["Lutador", "Veneno"],
        "desvantagens": ["Aço", "Psíquico"],
        "imunidades": ["Sombrio"]
    },
    "Inseto": {
        "vantagens": ["Planta", "Psíquico", "Sombrio"],
        "desvantagens": ["Fogo", "Lutador", "Veneno", "Voador", "Aço", "Fada"],
        "imunidades": []
    },
    "Pedra": {
        "vantagens": ["Fogo", "Gelo", "Voador", "Inseto"],
        "desvantagens": ["Lutador", "Terrestre", "Aço"],
        "imunidades": []
    },
    "Fantasma": {
        "vantagens": ["Psíquico", "Fantasma"],
        "desvantagens": ["Sombrio"],
        "imunidades": ["Normal"]
    },
    "Dragão": {
        "vantagens": ["Dragão"],
        "desvantagens": ["Aço"],
        "imunidades": ["Fada"]
    },
    "Sombrio": {
        "vantagens": ["Psíquico", "Fantasma"],
        "desvantagens": ["Lutador", "Sombrio", "Fada"],
        "imunidades": []
    },
    "Aço": {
        "vantagens": ["Gelo", "Pedra", "Fada"],
        "desvantagens": ["Fogo", "Água", "Elétrico", "Aço"],
        "imunidades": []
    },
    "Fada": {
        "vantagens": ["Lutador", "Dragão", "Sombrio"],
        "desvantagens": ["Fogo", "Veneno", "Aço"],
        "imunidades": []
    },
    "Normal": {
        "vantagens": [],
        "desvantagens": ["Pedra", "Aço"],
        "imunidades": ["Fantasma"]
    }
}

class TorneioPokemonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Torneio Campeões dos Campeões")
        self.geometry("850x650")
        self.resizable(False, False)
        
        # Lista para armazenar a equipe que o jogador escolher (0 a 3 Pokémon)
        self.equipe_jogador = []
        
        
        self.telas = {}
        for TelaClasse in (TelaMenu, TelaSelecao, TelaBatalha, TelaCampeao):
            nome_tela = TelaClasse.__name__
            frame = TelaClasse(parent=self, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.mostrar_tela("TelaMenu")

    def mostrar_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()


# ==========================================
# 1. TELA: MENU PRINCIPAL
# ==========================================
class TelaMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2c3e50")
        self.controller = controller
        
        tk.Label(self, text="Torneio Campeões dos Campeões", font=("Helvetica", 26, "bold"), bg="#2c3e50", fg="#f1c40f").pack(pady=60)
        tk.Label(self, text="“Use suas habilidades para se tornar o campeão dos campeões”", font=("Helvetica", 13, "italic"), bg="#2c3e50", fg="#ecf0f1").pack(pady=20)
        
        tk.Button(
            self, text="Iniciar Torneio", font=("Helvetica", 14, "bold"), 
            command=lambda: controller.mostrar_tela("TelaSelecao"),
            bg="#27ae60", fg="white", padx=30, pady=12, relief="raised", bd=3
        ).pack(pady=50)


# ==========================================
# 2. TELA: SELEÇÃO DE TREINADORES E POKÉMON
# ==========================================
class TelaSelecao(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#34495e")
        self.controller = controller
        
        #Dicionário para guardar as imagens dos pokémons
        self.image_salvas = {}
        
        tk.Label(self, text="Fase de Preparação", font=("Helvetica", 20, "bold"), bg="#34495e", fg="white").pack(pady=10)
        
        painel_principal = tk.Frame(self, bg="#34495e")
        painel_principal.pack(fill="both", expand=True, padx=20, pady=5)
        
        # --- LADO ESQUERDO: ÁRVORE DE CHAVES E LISTA ---
        lado_esquerdo = tk.Frame(painel_principal, bg="#34495e")
        lado_esquerdo.pack(side="left", fill="both", expand=True)
        
        # Grade de Adversários (Mata-Mata)
        tk.Label(lado_esquerdo, text="Adversários do Torneio (Mata-Mata):", bg="#34495e", fg="#e74c3c", font=("Helvetica", 12, "bold")).pack(anchor="w")
        grade_treinadores = tk.Frame(lado_esquerdo, bg="#2c3e50", pady=8, bd=1, relief="solid")
        grade_treinadores.pack(fill="x", pady=(5, 15))
        
        # Mostra os campeões listados no seu plano
        campeoes = ["Leon", "Cynthia", "Steven", "Lance", "Diantha", "Alain", "Iris", "Ash"]
        for i, cax in enumerate(campeoes):
            #Criação de um frame para cada treinador
            frame_treinador = tk.Frame(grade_treinadores, bg="#2c3e50")
            frame_treinador.grid(row=i//4, column=i%4, padx=12, pady=5)
            
            #Tentativa de carregar as fotos
            foto_treinador = self.carregar_imagem_segura(f'imagens/{cax.lower()}.png', tamanho=(50,50))
            lbl_foto = tk.Label(frame_treinador, image=foto_treinador, bg="#2c3e50")
            lbl_foto.image = foto_treinador
            lbl_foto.pack()
            
            tk.Label(frame_treinador, text=cax, bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 9, "bold")).pack()
            grade_treinadores.grid_columnconfigure(i%4, weight=1)
            
        # Lista de Seleção do Jogador
        tk.Label(lado_esquerdo, text="Escolha a sua Equipe (Clique para detalhar):", bg="#34495e", fg="#3498db", font=("Helvetica", 12, "bold")).pack(anchor="w")
        
        self.lista_pokemon = tk.Listbox(lado_esquerdo, height=10, font=("Helvetica", 12, "bold"), bg="#ecf0f1", selectbackground="#3498db")
        self.lista_pokemon.pack(fill="both", expand=True, pady=5)
        
        # Popula a lista com os 10 Pokémon reais do seu plano
        for poke in DADOS_POKEMON.keys():
            self.lista_pokemon.insert(tk.END, poke)
            
        self.lista_pokemon.bind("<<ListboxSelect>>", self.atualizar_painel_lateral)
        
        # --- PAINEL DO TIME ESCOLHIDO (FOTOS DE PERFIL) ---
        tk.Label(lado_esquerdo, text='Sua Equipe Atual:', bg="#34495e", fg="#2ecc71", font=("Helvetica", 11, "bold")).pack(anchor="w")
        self.frame_time = tk.Frame(lado_esquerdo, bg="#2c3e50", height=60, bd=2, relief="sunken")
        self.frame_time.pack(fill="x", pady=5)
        #Mantém o tamanho fixo
        self.frame_time.pack_propagate(False) 
        
        # --- LADO DIREITO: PAINEL SIMULTÂNEO DE DETALHES ---
        self.lado_direito = tk.Frame(painel_principal, bg="#2c3e50", width=340, bd=3, relief="ridge")
        self.lado_direito.pack(side="right", fill="both", padx=(20, 0))
        self.lado_direito.pack_propagate(False)
        
        # Labels Dinâmicos do Painel Direito
        
        self.lbl_nome = tk.Label(self.lado_direito, text="Selecione um Pokémon", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#f1c40f")
        self.lbl_nome.pack(pady=10)
        
        #Espaço reservado para a foto do pokémon em destaque
        self.lbl_foto_destaque = tk.Label(self.lado_direito, bg="#2c3e50")
        self.lbl_foto_destaque.pack(pady=5)
        
        self.lbl_tipo = tk.Label(self.lado_direito, text="Tipo: ---", font=("Helvetica", 11, "bold"), bg="#2c3e50", fg="#4bc0c0")
        self.lbl_tipo.pack(anchor="w", padx=15)
        
        self.lbl_status = tk.Label(self.lado_direito, text="STATUS BASE:\n• Ataque: -\n• Defesa: -\n• Velocidade: -", font=("Helvetica", 11), bg="#2c3e50", fg="white", justify="left")
        self.lbl_status.pack(anchor="w", padx=15, pady=10)
        
        self.lbl_movimentos = tk.Label(self.lado_direito, text="MOVIMENTOS:\n- \n- ", font=("Helvetica", 11), bg="#2c3e50", fg="#e0e0e0", justify="left")
        self.lbl_movimentos.pack(anchor="w", padx=15, pady=5)
        
        tk.Label(self.lado_direito, text="ÊNFASE:", font=("Helvetica", 10, "bold"), bg="#2c3e50", fg="#f1c40f").pack(anchor="w", padx=15, pady=(10,0))
        self.lbl_enfase = tk.Label(self.lado_direito, text="As informações detalhadas do mutante de batalha vão aparecer aqui.", font=("Helvetica", 10, "italic"), bg="#2c3e50", fg="#bdc3c7", wraplength=300, justify="left")
        self.lbl_enfase.pack(anchor="w", padx=15, pady=2)
        
        # --- BOTÕES INFERIORES ---
        painel_botoes = tk.Frame(self, bg="#34495e")
        painel_botoes.pack(fill="x", pady=15)
        
        #Setei todos os botões na esquerda e usei o 'extend'
        #O extend calcula o tamanho dos botões o espaço que ele tem para dispor os botão e os organiza perfeitamente
        bnt_voltar = tk.Button(painel_botoes, text="Voltar ao Menu", bg="#e74c3c", fg="white", font=("Helvetica", 11, "bold"), command=self.voltar_ao_menu)
        bnt_voltar.pack(side="left", expand=True, padx=20)
        
        self.btn_adicionar = tk.Button(painel_botoes, text="Adicionar à Equipe (0/3)", bg="#3498db", fg="white", font=("Helvetica", 11, "bold"), command=self.adicionar_a_equipe)
        self.btn_adicionar.pack(side="left", expand=True, padx=20)
        
        btn_confirmar = tk.Button(painel_botoes, text="Confirmar Torneio", bg="#27ae60", fg="white", font=("Helvetica", 11, "bold"), command=self.confirmar_equipe_final)
        btn_confirmar.pack(side="left", expand=True, padx=20)
        
        
    def voltar_ao_menu(self):
        """Limpa as escolhas atuais e volta para o menu inicial"""
        #Zera a lista global do jogador
        self.controller.equipe_jogador.clear()
        #Lógica:
        #Equipe_jogador é um ponteiro que aponta para a nossa lista onde está nossa equipe,
        # sendo assim, faço o uso do clear para reiniciar os elementos dessa lista
        
        #Destroi as fotos pequenas na aba "Sua Equipe Atual"
        for widget in self.frame_time.winfo_children():
            widget.destroy()
        #Lógica:
        #No tkinter se eu apenas escondece a tela de seleção as imagens que são tratadas como Labels
        # ainda continuariam na tela, possibilitando bugs de sobrepossição dentre outros.
        #Por isso usei o winfo.children junto com o destroy. Assim o 1° limpa a arvore de componentes e o segundo fecha a janela(reinicia)
        
        #Reseta o texto do botão de adicionar
        self.btn_adicionar.config(text="Adicionar à Equipe (0/3)")
        
        #Troca a tela
        self.controller.mostrar_tela("telaMenu")
        #lógica:
        #Aqui é uma pura manipulação de pilhas. Eu apenas fiz o tkinter puxar
        # a telaMenu para frente das demais 
        
    def carregar_imagem_segura(self, caminho, tamanho=(50, 50)):
        """Tenta carregar uma imagem. Se o arquivo não existir, cria um quadrado cinza genérico."""
        if os.path.exists(caminho): # "path.exists(caminho) é a busca/ verificação se existe um arquivo no "caminho"
            img = Image.open(caminho).resize(tamanho, Image.Resampling.NEAREST)
            #resize: Pega a imgem e redimenciona 
            #Image.Resamplin.LANCZOS: Filtro da biblioteca Pillow para ao redimencionar manter a nitidez
        else:
            #Quadrado cinza como reserva de espaço caso não tenha foto
            img =Image.new('RGB', tamanho, color='#7f8c8d')
        return ImageTk.PhotoImage(img)

    def atualizar_painel_lateral(self, event):
        """Lê os dados do dicionário e atualiza a interface dinamicamente"""
        selecao = self.lista_pokemon.curselection()
        if selecao:
            nome = self.lista_pokemon.get(selecao[0])
            infos = DADOS_POKEMON[nome]
            
            # Atualiza os textos da interface gráfica
            self.lbl_nome.config(text=nome)
            self.lbl_tipo.config(text=f"Tipo: {' / '.join(infos['tipos'])}")
            
            texto_status = f"STATUS BASE:\n• HP: {infos['hp']}\n• Ataque: {infos['ataque']}\n• Ataque Especial: {infos['ataque_especial']}\n• Defesa: {infos['defesa']}\n• Defesa Especial: {infos['defesa_especial']}\n• Velocidade: {infos['velocidade']}"
            self.lbl_status.config(text=texto_status)
            
            # texto_moves = "MOVIMENTOS:\n" + "\n"([f"• {m}" for m in infos["movimentos"]])
            # for m in infos["movimentos"]:
            texto_moves = "MOVIMENTOS:\n"
            for m in infos["movimentos"]:
                save_categoria = infos["movimentos"][m]["categoria"]
                save_tipo = infos["movimentos"][m]["tipo"]
                texto_moves += f"• {m} ({save_tipo} - {save_categoria})\n"
            
                
            #config altera uma propriedade de algo na tela em tempo real.
            self.lbl_movimentos.config(text=texto_moves)
            
            self.lbl_enfase.config(text=f'"{infos["enfase"]}"')
            
            #Atualizar Image do Pokémon (Tamanho Maior)
            foto_destaque = self.carregar_imagem_segura(f"imagens/{nome.lower()}.png", tamanho=(100, 100))
            self.lbl_foto_destaque.config(image=foto_destaque)
            self.lbl_foto_destaque.image = foto_destaque #Salva referência para não perder

    def adicionar_a_equipe(self):
        selecao = self.lista_pokemon.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um Pokémon na lista primeiro!")
            return
            
        nome = self.lista_pokemon.get(selecao[0])
        
        if nome in self.controller.equipe_jogador:
            messagebox.showwarning("Aviso", f"O {nome} já está na sua equipe!")
            return
            
        if len(self.controller.equipe_jogador) >= 3:
            messagebox.showwarning("Aviso", "A sua equipe já está cheia! (Máximo de 3 Pokémon)")
            return
            
        # Adiciona o Pokémon à lista global da aplicação
        self.controller.equipe_jogador.append(nome)
        qtd = len(self.controller.equipe_jogador)
        self.btn_adicionar.config(text=f"Adicionar à Equipe ({qtd}/3)")
        
        # Adiciona a foto pequena do pokémon na barra "Sua Equipe Atual"
        foto_time = self.carregar_imagem_segura(f"imagens/{nome.lower()}.png", tamanho=(40, 40))
        lbl_icone = tk.Label(self.frame_time, image=foto_time, bg="#2c3e50")
        lbl_icone.image = foto_time
        lbl_icone.pack(side="left", padx=10, pady=5)
    def confirmar_equipe_final(self):
        qtd = len(self.controller.equipe_jogador)
        if qtd == 0:
            messagebox.showwarning("Aviso", "Escolha pelo menos 1 Pokémon para iniciar o torneio!")
            return
            
        resposta = messagebox.askyesno("Confirmação Importante", f"Deseja entrar no Torneio com estes {qtd} Pokémon?\nEquipe: {', '.join(self.controller.equipe_jogador)}")
        if resposta:
            self.controller.mostrar_tela("TelaBatalha")
    
# ==========================================
# 3. TELA: TELA DE BATALHA
# ==========================================
num_turno = 0

class TelaBatalha(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#bdc3c7")
        self.controller = controller
        self.gerenciador = None
        
        # Área superior de simulação visual
        self.area_combate = tk.Frame(self, bg="#ecf0f1", height=320, bd=2, relief="sunken")
        self.area_combate.pack(fill="x", padx=20, pady=15)
        self.area_combate.pack_propagate(False)
        
        # HUD Inimigo
        self.frame_bloco_inimigo = tk.Frame(self.area_combate, bg="#ecf0f1")
        self.frame_bloco_inimigo.pack(anchor="ne", padx=20, pady=10)
        
        self.hud_inimigo = tk.Frame(self.frame_bloco_inimigo, bg="#ecf0f1")
        self.hud_inimigo.pack(side="left", padx=10)
        
        self.lbl_nome_inimigo = tk.Label(self.hud_inimigo, text="Inimigo", bg="#ecf0f1", font=("Helvetica", 11, "bold"))
        self.lbl_nome_inimigo.pack(anchor="e")
        self.hp_inimigo_bar = tk.Frame(self.hud_inimigo, bg="#27ae60", width=180, height=18)
        self.hp_inimigo_bar.pack(anchor="e")

        # Espaço reservado para a FOTO do Pokémon Inimigo
        self.lbl_foto_inimigo = tk.Label(self.frame_bloco_inimigo, bg="#ecf0f1")
        self.lbl_foto_inimigo.pack(side="right")
        
        # HUD Jogador
        self.hud_jogador = tk.Frame(self.area_combate, bg="#ecf0f1")
        self.hud_jogador.pack(anchor="sw", padx=20, pady=60)
        self.lbl_nome_jogador = tk.Label(self.hud_jogador, text="Seu Pokémon", bg="#ecf0f1", font=("Helvetica", 11, "bold"))
        self.lbl_nome_jogador.pack(anchor="w")
        self.hp_jogador_bar = tk.Frame(self.hud_jogador, bg="#27ae60", width=180, height=18)
        self.hp_jogador_bar.pack(anchor="w")
        
        # Caixa de Comandos / Hotbar Inferior
        self.janela_comandos = tk.Frame(self, bg="#2c3e50", height=180)
        self.janela_comandos.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        self.hotbar_ataques = tk.Frame(self.janela_comandos, bg="#2c3e50")
        self.hotbar_ataques.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.botoes_ataque = []

        def configurar_torneio(self):
            self.gerenciador = GerenciadorTorneio(self.controller.equipe_jogador)
            self.gerenciador.iniciar_proxima_rodada()
            self.atualizar_interface_batalha()

        def atualizar_interface_batalha(self):
            # Dados do Jogador j = jogador, i = inimigo
            poke_j = self.gerenciador.pokemon_jogador_atual
            nome_j = self.gerenciador.equipe_jogador[self.gerenciador.index_jogador]
            self.lbl_nome_jogador.config(text=f"{nome_j} (HP: {poke_j['hp']}/{poke_j['max_hp']})")
            
            # Dados do Rival
            poke_i = self.gerenciador.pokemon_inimigo_atual
            treinador_i = self.gerenciador.treinador_inimigo
            nome_i = self.gerenciador.mapa_pokemon_treinador[treinador_i]
            self.lbl_nome_inimigo.config(text=f"{nome_i} de {treinador_i} (HP: {poke_i['hp']}/{poke_i['max_hp']})")
            
            # Atualizar Barras de HP de forma proporcional (Largura max: 180px)
            largura_j = int((poke_j['hp'] / poke_j['max_hp']) * 180) if poke_j['hp'] > 0 else 0
            largura_i = int((poke_i['hp'] / poke_i['max_hp']) * 180) if poke_i['hp'] > 0 else 0
            self.hp_jogador_bar.config(width=max(0, largura_j))
            self.hp_inimigo_bar.config(width=max(0, largura_i))
            
            # Limpar botões antigos da Hotbar
            for btn in self.botoes_ataque:
                btn.destroy()
            self.botoes_ataque.clear()
            
            # Criar botões dinâmicos com os ataques reais do Pokémon atual do jogador
            movimentos = list(poke_j["movimentos"].keys())
            for i, move_nome in enumerate(movimentos):
                btn = tk.Button(
                    self.hotbar_ataques, text=move_nome, font=("Helvetica", 11, "bold"),
                    bg="#3498db", fg="white",
                    command=lambda m=move_nome: self.executar_turno(m)
                )
                btn.grid(row=i//2, column=i%2, sticky="nsew", padx=5, pady=5)
                self.hotbar_ataques.grid_columnconfigure(i%2, weight=1)
                self.hotbar_ataques.grid_rowconfigure(i//2, weight=1)
                self.botoes_ataque.append(btn)

        def executar_turno(self, movimento_escolhido):
            
            if self.num_turnos == 0:
                atacante, defensor = self.gerenciador.ataca_primeiro(poke_j, poke_i)
                save_atacante = atacante
                save_defensor = defensor
                
            elif self.num_turnos % 2 != 0:
                atacante = save_defensor
                defensor = save_atacante
                
            else:
                atacante = save_atacante
                defensor = save_defensor
            
            
            poke_j = self.gerenciador.pokemon_jogador_atual
            poke_i = self.gerenciador.pokemon_inimigo_atual
            
            # 1. ATAQUE DO JOGADOR
            dano_j = self.gerenciador.calcular_e_aplicar_dano(poke_j, poke_i, movimento_escolhido)
            poke_i["hp"] -= dano_j
            messagebox.showinfo("Batalha", f"{self.lbl_nome_jogador.cget('text').split()[0]} usou {movimento_escolhido} e causou {dano_j} de dano!")
            
            # Checa se o inimigo desmaiou
            if poke_i["hp"] <= 0:
                poke_i["hp"] = 0
                self.atualizar_interface_batalha()
                messagebox.showinfo("Vitória!", f"Você derrotou o {self.lbl_nome_inimigo.cget('text').split()[0]}!")
                
                if len(self.gerenciador.ordem_combate) > 0:
                    self.gerenciador.iniciar_proxima_rodada()
                    self.atualizar_interface_batalha()
                else:
                    self.controller.mostrar_tela("TelaCampeao")
                return

            # 2. CONTRA-ATAQUE DO INIMIGO
            movimentos_inimigo = list(poke_i["movimentos"].keys())
            move_inimigo = random.choice(movimentos_inimigo)
            dano_i = self.gerenciador.calcular_e_aplicar_dano(poke_i, poke_j, move_inimigo)
            poke_j["hp"] -= dano_i
            messagebox.showinfo("Batalha", f"{self.lbl_nome_inimigo.cget('text').split()[0]} inimigo usou {move_inimigo} e causou {dano_i} de dano!")
            
            # Checa se o jogador desmaiou
            if poke_j["hp"] <= 0:
                poke_j["hp"] = 0
                self.atualizar_interface_batalha()
                
                # Tenta puxar o próximo Pokémon vivo da equipe escolhida
                self.gerenciador.index_jogador += 1
                if self.gerenciador.index_jogador < len(self.gerenciador.equipe_jogador_viva):
                    self.gerenciador.pokemon_jogador_atual = self.gerenciador.equipe_jogador_viva[self.gerenciador.index_jogador]
                    messagebox.showinfo("Substituição", f"Seu Pokémon desmaiou! Vai, {self.gerenciador.equipe_jogador[self.gerenciador.index_jogador]}!")
                else:
                    messagebox.showerror("Fim de Jogo", "Todos os seus Pokémon desmaiaram! Você foi eliminado do torneio.")
                    self.controller.mostrar_tela("TelaMenu")
                    return

            self.atualizar_interface_batalha()
            
            num_turno += 1

class GerenciadorTorneio:
    def __init__(self, equipe_jogador_da_interface):
        self.equipe_jogador_viva = []
        
        for nome_pokemon in equipe_jogador_da_interface:
            self.equipe_jogador_viva.append(copy.deepcopy(DADOS_POKEMON[nome_pokemon]))
        
        self.equipe_jogador = equipe_jogador_da_interface
        self.index_jogador = 0

        campeoes_base = ["Leon", "Cynthia", "Steven", "Lance", "Diantha", "Alain", "Iris", "Ash"]
        #Cria a ordem de combate
        self.ordem_combate = list(campeoes_base)
        random.shuffle(self.ordem_combate)
        #Salva quem está na batalha
        self.pokemon_jogador = None
        self.pokemon_inimigo = None
        self.treinador_inimigo = None
        self.mapa_pokemon_treinador = {
            "Leon": "Charizard",
            "Cynthia": "Garchomp",
            "Steven": "Metagross",
            "Lance": "Dragonite",
            "Diantha": "Gardevoir",
            "Alain": "Tyranitar",
            "Iris": "Lapras",
            "Ash": "Pikachu"
        }    
    
    def iniciar_proxima_rodada(self):
    #     #Puxa o nome do treinador da lista randomizada
        self.treinador_inimigo = self.ordem_combate.pop(0)
        
        nome_pokemon_inimigo = self.mapa_pokemon_treinador[self.treinador_inimigo]
        
    #     #ERRO MENCIONADO EM SALA: 
    #     # Aqui os dicionários tem um espaço definido na memória e quando faço x = dicionário
    #     # ele apenas cria um outro nome que aponta para a mesma coisa.
    #     #self.pokemon_inimigo == DADOS_POKEMON_TREINADORES[nome_pokemon]

    #     #PROBLEMA:
    #     # Se eu no futuro alterar o valor da vida do pokemon essa alteração vai ser salva no banco de dados original
    #     #self.pokemon_inimigo_atual["hp"] -= 40
        
    #     #SOLUÇÃO:
        # importei uma biblioteca "copy" que cria um clone do dicionário, assim, problema resolvido :)
        
        # #Puxa as informações do pokemon inimigo
        self.pokemon_inimigo_atual = copy.deepcopy(DADOS_POKEMON_TREINADORES[nome_pokemon_inimigo])
    
        self.pokemon_jogador_atual = self.equipe_jogador_viva[self.index_jogador]
    
    # def calcular_e_aplicar_dano(self, atacante, defensor, movimento_nome):
    #     movimento = atacante["movimentos"][movimento_nome]
        
    #     if movimento["categoria"] == "Físico":
    #         pwr_ataque = atacante["ataque"]
    #         pwr_defesa = defensor["defesa"]
    #     else:
    #         pwr_ataque = atacante["ataque_especial"]
    #         pwr_defesa = defensor["defesa_especial"]
            
    #     # Fórmula matemática balanceada de dano base
    #     dano = int((pwr_ataque / pwr_defesa) * 20) + random.randint(5, 15)
    #     return max(5, dano)
    
    def ataca_primeiro(self,pokemon_1, pokemon_2):
        self.poke_j_velocidade = DADOS_POKEMON[pokemon_1]["velocidade"]
        self.poke_i_velocidade = DADOS_POKEMON_TREINADORES[pokemon_2]["velocidade"]
        if self.poke_i_velocidade >= self.poke_j_velocidade:
            atacante = pokemon_2
            defensor = pokemon_1
            
        else:
            atacante = pokemon_1
            defensor = pokemon_2
        return atacante, defensor
    
    def verificar_afinidade_pura(self, tipo_ataque, tipo_defensor_unico):
        # Se o tipo do defensor estiver na lista de vantagens do ataque...
        if tipo_defensor_unico in TABELA_TIPAGENS[tipo_ataque]["vantagens"]:
            return 2.0
        
        # Se o tipo do defensor estiver na lista de desvantagens...
        elif tipo_defensor_unico in TABELA_TIPAGENS[tipo_ataque]["desvantagens"]:
            return 0.5
        
        # Se o tipo do defensor estiver na lista de imunidades...
        elif tipo_defensor_unico in TABELA_TIPAGENS[tipo_ataque]["imunidades"]:
            return 0.0
        
        # Se não estiver em nenhuma lista (Normal/Neutro)
        else:
            return 1.0
    
    def vantagem_tipagem(self,pokemon_1,pokemon_2, movimento_escolhido):
        tipagem = pokemon_1["movimentos"][movimento_escolhido]["tipo"]
        tipagem_pokemon_adversário = pokemon_2["tipos"]
        multi = 1.0
        for i in tipagem_pokemon_adversário:
            multi_tipagem = self.verificar_afinidade_pura(tipagem,i)
            
            multi = multi * multi_tipagem
        return multi
        
    def calcular_e_aplicar_dano(self, atacante, defensor, movimento_escolhido):
        
        
        
        if random.random() > 0.95:
            dano_base = 0
        
            categoria_do_movimento = atacante["movimentos"][movimento_escolhido]["categoria"]
        dano_final = dano_base * multiplicador_critico * fator_aleatorio
        dano_final = int(dano_final // 1)
    
    def escolhar_ataque_inimigo(sellf, pokemon_inimigo, pokemon_jogador):
        lista_de_golpe = list(pokemon_inimigo["movimentos"].keys())
        multi_dos_golpes = {}
        
        for golpe in lista_de_golpe:
            multi = self.vantagem_tipagem(pokemon_inimigo, pokemon_jogador, golpe)
            multi_dos_golpes[golpe] = multi
            
        maior_multi = max(multi_dos_golpes.values())
        
        melhores_golpes = []
        
        for golpe, nota in multi_dos_golpes.items():
            if nota == maior_multi:
                melhores_golpes.append(golpe)
        valor_random = random.random()
        
        if valor_random <= 0.75:
            ataque_escolhido = random.choice(melhores_golpes)
        else:
            ataque_escolhido = random.choice(lista_de_golpe)
        
        return ataque_escolhido
        
# ==========================================
# 4. TELA: CAMPEÃO (FIM DE JOGO)
# ==========================================

class TelaCampeao(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f1c40f")
        
        tk.Label(self, text="🏆", font=("Helvetica", 90), bg="#f1c40f").pack(pady=40)
        
        self.lbl_vitoria = tk.Label(
            self, text="Parabéns Treinador,\nvocê é o novo Monarca da Liga!\nO treinador pokémon mais forte!", 
            font=("Helvetica", 20, "bold"), bg="#f1c40f", fg="#2c3e50", justify="center"
        )
        self.lbl_vitoria.pack(pady=20)
        
        tk.Button(
            self, text="Jogar Novamente", font=("Helvetica", 12, "bold"),
            command=lambda: controller.mostrar_tela("TelaMenu"), bg="#2c3e50", fg="white", padx=15, pady=8
        ).pack(pady=30)

if __name__ == "__main__":
    app = TorneioPokemonApp()
    app.mainloop()
