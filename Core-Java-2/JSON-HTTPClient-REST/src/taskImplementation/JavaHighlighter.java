package taskImplementation;

import java.io.*;
import java.util.*;
import java.util.logging.*;

import javax.swing.*;

import syntaxhighlight.SyntaxHighlighter;
import syntaxhighlighter.brush.*;
import syntaxhighlighter.SyntaxHighlighterParser;
import syntaxhighlighter.theme.*;

public class JavaHighlighter {

  public static void main(String[] args) {
    SwingUtilities.invokeLater(new Runnable() {

      @Override
      public void run() {
        // the SyntaxHighlighter parser
        SyntaxHighlighterParser parser = new SyntaxHighlighterParser(new BrushJava());
        // turn HTML script on
        parser.setHtmlScript(true);
        // set HTML Script brushes
        parser.setHTMLScriptBrushes(Arrays.asList(new BrushJava()));

        SyntaxHighlighter highlighter = new SyntaxHighlighter(parser, new ThemeMidnight());
        
        highlighter.setHighlightedLineList(Arrays.asList(1,2,3,4,5));
        try {
          highlighter.setContent(new File("test.java"));
        } catch (IOException ex) {
          Logger.getLogger(JavaHighlighter.class.getName()).log(Level.SEVERE, null, ex);
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