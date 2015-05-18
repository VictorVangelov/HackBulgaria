package taskImplementation;

import java.io.*;
import java.util.*;
import java.util.logging.*;
import javax.swing.*;
import syntaxhighlighter.SyntaxHighlighter;
import syntaxhighlighter.brush.*;
import syntaxhighlighter.SyntaxHighlighterParser;
import syntaxhighlighter.theme.ThemeRDark;

public class Example {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {

            @Override
            public void run() {
                // the SyntaxHighlighter parser
                SyntaxHighlighterParser parser = new SyntaxHighlighterParser(
                        new BrushXml());
                // turn HTML script on
                parser.setHtmlScript(true);
                // set HTML Script brushes
                parser.setHTMLScriptBrushes(Arrays.asList(new BrushCss(),
                        new BrushJava()));
                try {
                    highlighter.setContent(new File("test.html"));
                } catch (IOException ex) {
                    Logger.getLogger(Example.class.getName()).log(Level.SEVERE,
                            null, ex);
                }

                JFrame frame = new JFrame();
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setContentPane(highlighter);
                frame.setLocationByPlatform(true);
                frame.pack();
                frame.setVisible(true);
            }
        });
    }
}
