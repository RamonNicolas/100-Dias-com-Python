from app import manager
from logging import debug

# Rodando a aplicacao
# Debug True assim que qualquer alteracao for feita ele atualiza
if __name__ == "__main__":
    manager.run(debug=True)
