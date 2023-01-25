from log import LogPrintMixins, LogFileMixin

class Eletronico:
    def __init__(self, marca):
        self.marca = marca
        self.is_on = False

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = True

class Celular(Eletronico):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

        self.__log_print = LogPrintMixins()
        self.__log_file = LogFileMixin()
    
    def on(self):
        msg_erro =  f"{self.marca} {self.modelo} já está Ligado!"
        msg_sucess = f"{self.marca} {self.modelo} está ligado!"

        if self.is_on:
            self.__log_file.log_error(msg_erro)
            return self.__log_print.log_error(msg_erro)
            

        super().on()
        self.__log_file.log_sucess(msg_sucess)
        return self.__log_print.log_sucess(msg_sucess)

    def off(self):
        msg_erro =  f"{self.marca} {self.modelo} já está Desligado!"
        msg_sucess = f"{self.marca} {self.modelo} está desligado!"

        if not self.is_on:
            self.__log_file.log_error(msg_erro)
            return self.__log_print.log_error(msg_erro)

        super().off()
        self.__log_file.log_sucess(msg_sucess)
        return self.__log_print.log_sucess(msg_sucess)