import java.security.SecureRandom;

public class PasswordGenerator {

    private static final String LOWER = "abcdefghijklmnopqrstuvwxyz";
    private static final String UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String DIGITS = "0123456789";
    private static final String SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?";

    public static String generatePassword(int length) {
        String allChars = LOWER + UPPER + DIGITS + SPECIAL;
        SecureRandom random = new SecureRandom();
        StringBuilder password = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(allChars.length());
            password.append(allChars.charAt(randomIndex));
        }

        return password.toString();
    }

    public static void main(String[] args) {
        int passwordLength = 12; // Set the desired password length
        String generatedPassword = generatePassword(passwordLength);
        System.out.println("Generated Password: " + generatedPassword);
    }
}