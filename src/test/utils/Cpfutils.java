package test.utils;

public class Cpfutils {

    public static boolean validarCPF(String cpf) {
        cpf = cpf.replaceAll("[^\\d]", "");

        if (cpf.length() != 11 || cpf.chars().distinct().count() == 1) {
            return false; // CPF inválido ou todos os dígitos iguais
        }

        // Cálculo do primeiro dígito verificador
        int soma1 = 0;
        for (int i = 0; i < 9; i++) {
            soma1 += Character.getNumericValue(cpf.charAt(i)) * (10 - i);
        }
        int dv1 = soma1 % 11 < 2 ? 0 : 11 - (soma1 % 11);

        // Cálculo do segundo dígito verificador
        int soma2 = 0;
        for (int i = 0; i < 9; i++) {
            soma2 += Character.getNumericValue(cpf.charAt(i)) * (11 - i);
        }
        soma2 += dv1 * 2;
        int dv2 = soma2 % 11 < 2 ? 0 : 11 - (soma2 % 11);

        // Verificação final
        return cpf.endsWith("" + dv1 + dv2);
    }

    // Exemplo de uso
    public static void main(String[] args) {
        String cpfTeste = "123.456.789-09";
        System.out.println("CPF válido? " + validarCPF(cpfTeste));
    }
}
