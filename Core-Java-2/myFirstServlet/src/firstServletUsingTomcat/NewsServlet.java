package firstServletUsingTomcat;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class firstExampleUsageTomcat
 */
@WebServlet("/news")
public class NewsServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public NewsServlet() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		String content = "asd";
		try {
			content = NewsGetter.getNews();
			Thread.sleep(1000);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


		response.setContentType("text/html; charset=UTF-8");
		response.getWriter().print(
				"<h1>This is the leadest news int our corrruped country</h1>");
		response.getWriter().print(content);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
