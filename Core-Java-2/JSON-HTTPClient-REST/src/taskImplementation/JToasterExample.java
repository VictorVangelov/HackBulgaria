package taskImplementation;

import java.awt.Color;
import java.awt.Image;

import com.nitido.utils.toaster.*;

import javax.swing.*;

public class JToasterExample {
	public static void main(String[] args) throws InterruptedException {
		while (true) {
			ToastMe();
			Thread.sleep(1000*10);
		}

	}

	private static void ToastMe() throws InterruptedException {
		ImageIcon toastedIcon = new ImageIcon("handJob.jpg");
		int iconHight = toastedIcon.getIconHeight();
		int iconWidth = toastedIcon.getIconWidth();
		Image toastImage = toastedIcon.getImage();
		Toaster toasterManager = new Toaster();
		toasterManager.setDisplayTime(1000 * 5); // 15sec
		// toasterManager.setStep(1000*15);
		toasterManager.setToasterHeight(iconHight);
		toasterManager.setToasterWidth(iconWidth);
		toasterManager.setBackgroundImage(toastImage);
		toasterManager.setBorderColor(Color.cyan);
		toasterManager
				.showToaster("Too much work, take a break and take care for your head ;) \n You have 5 minutes");
		Thread.sleep(5000);

	}

}
