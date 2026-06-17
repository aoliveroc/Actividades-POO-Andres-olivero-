import math

class CálculosNuméricos:
    
    @staticmethod
    def logaritmo(valor):
        """
        Calcula el logaritmo de un valor.
        
        Args:
            valor (float): El valor para calcular el logaritmo
            
        Returns:
            float: El logaritmo del valor
            
        Raises:
            ArithmeticError: Si el valor no es positivo
        """
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo")
        return math.log10(valor)  # Logaritmo en base 10
    
    @staticmethod
    def raizCuadrada(valor):
        """
        Calcula la raíz cuadrada de un valor.
        
        Args:
            valor (float): El valor para calcular la raíz cuadrada
            
        Returns:
            float: La raíz cuadrada del valor
            
        Raises:
            ArithmeticError: Si el valor no es positivo
        """
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada")
        return math.sqrt(valor)
    
    @staticmethod
    def main():
        """
        Método principal que solicita un valor por teclado y realiza los cálculos.
        """
        try:
            
            valor = float(input("Valor numérico = "))
            
            
            try:
                resultado_log = CálculosNuméricos.logaritmo(valor)
                print(f"Logaritmo: {resultado_log:.6f}")
            except ArithmeticError as e:
                print(e)
            
           
            try:
                resultado_raiz = CálculosNuméricos.raizCuadrada(valor)
                print(f"Raíz cuadrada: {resultado_raiz:.6f}")
            except ArithmeticError as e:
                print(e)
                
        except ValueError:
            print("Error: Debe ingresar un número válido.")


if __name__ == "__main__":
    CálculosNuméricos.main()
