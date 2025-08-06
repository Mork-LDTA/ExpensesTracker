package test.utils;

public class test extends Cpfutils{
    public static void main(String[] args) {
        String cpfTeste = "123.456.789-09";
        System.out.println("CPF válido? " + validarCPF(cpfTeste));
    }
}
