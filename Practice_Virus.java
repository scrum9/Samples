import java.util.Random;
import java.swig.JLabel;
import java.awt.event.KeyEvent;
import java.swing.JWindow;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.Dimension;


public class PracticeVirus{
    private final Dimension screenSize = Toolkit.getDefualtToolkit().getScreenSize();
    private final int height = (int) screenSize.getHeight();
    private final int width = (int) screenSize.getWidth();
    private final Random Randm = new Random();

public void BlockAll() throws AWTException
{
    Robot _robot = new Robot();
    _robot.keyPress(KeyEvent.VK_0);
    _robot.mouseMove(Randm.nextInt(width),Randm.nextInt(height));

}
public void Popup()
{
    JWindow window = new JWindow();
    JLabel label = new JLabel( text: "You have been infected! Get Wrecked!")
    window.add(label);
    window.setSize(width: 150, height: 50);
    window.setLocation(Randm.nextInt(width), Randm.nextInt(height));
    window.setVisible(true);
}

public static void main(String[] args) throws AWTException, InterruptedException {
    PracticeVirus fv = new PracticeVirus():

    while(true)
    {
        fv.BlockAll();
        fv.Popup();
    }
}

}
