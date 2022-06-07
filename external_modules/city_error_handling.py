class City_Error_Handling(Exception):    # ok
    def __init__(self,message:str) -> None:
        super().__init__(message)
        self.__message=message
    def __str__(self) -> str:
        return f"the problem :{self.__message}"


if __name__=="__main__":
    x=City_Error_Handling('City not found')
    print(x)