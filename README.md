# Gym UEMA
> Este projeto foi desenvolvido como requisito para obtenção de nota na disciplina de Gestão de Projetos. Logo após, serviu como sistema para criação de um container Docker para a disciplina de sistema Distribuídos.

## Instalação via Ambiente Virtual
```sh
python -m venv venv
```

Ative o ambiente virtual (Windows)
```sh
.\venv\Scripts\activate
```

Ative o ambiente virtual (Linux)
```sh
./venv/bin/activate
```

Instale as dependências
```sh
pip install -r requirements.txt
```

### Aplique as migrations
```sh
python manage.py migrate
```

### Executando o servidor com a aplicação
```sh
python manage.py runserver
```

Um servidor Django estará rodando localmente na URL: http://127.0.0.1:8000/