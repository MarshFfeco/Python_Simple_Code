from pathlib import Path

LOG_FILE = Path(__file__).parent / 'logs' / 'log.txt'

class Logs:
    def _log(self, msg):
        raise NotImplementedError("Implement o método Log")
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_sucess(self, msg):
        return self._log(f"Sucess: {msg}")

class LogFileMixin(Logs):
    def _log(self, msg):
        arquivo_formatado = f'{msg} de ({self.__class__.__name__})'

        with open(LOG_FILE, 'a', encoding="utf-8") as file:
            file.write('### ---------------------- ###### ---------------------- \n')
            file.write(f'{arquivo_formatado}\n')
            file.write('\n')

class LogPrintMixins(Logs):
    def _log(self, msg):
        print(f'{msg} de ({self.__class__.__name__})')

if __name__ == "__main__":
    lf = LogFileMixin()
    lf.log_error("Erro ao acessar!")
    lf.log_sucess("Sucesso ao acessar!")

    lp = LogPrintMixins()
    lp.log_error("Erro ao acessar!")
    lp.log_sucess("Sucess ao acessar!")