import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.TargetDataLine;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;

import javax.swing.SwingUtilities;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JLabel;


public class AudioVisualizer extends JFrame {

    private static final int CHUNK_SIZE = 1024;
    private static final int AMPLIFICATION_FACTOR = 2;

    private JLabel statusLabel;
    private JPanel graphPanel;

    public AudioVisualizer() {
        setTitle("Audio Visualizer");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        statusLabel = new JLabel("Listening...");
        add(statusLabel, BorderLayout.NORTH);

        graphPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawGraph(g);
            }
        };
        graphPanel.setPreferredSize(new Dimension(800, 400));
        add(graphPanel, BorderLayout.CENTER);

        pack();
        setVisible(true);

        captureAudio();
    }

    private void drawGraph(Graphics g) {
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, graphPanel.getWidth(), graphPanel.getHeight());

        g.setColor(Color.GREEN);

        for (int i = 0; i < CHUNK_SIZE - 1; i++) {
            int x1 = i * 2;
            int y1 = (int) (Math.random() * 32768 * AMPLIFICATION_FACTOR);
            int x2 = (i + 1) * 2;
            int y2 = (int) (Math.random() * 32768 * AMPLIFICATION_FACTOR);
            g.drawLine(x1, y1, x2, y2);
        }
    }

    private void captureAudio() {
        try {
            AudioFormat format = new AudioFormat(44100, 16, 1, true, false);
            DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

            if (!AudioSystem.isLineSupported(info)) {
                statusLabel.setText("Line not supported");
                return;
            }

            TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
            line.open(format);
            line.start();

            byte[] buffer = new byte[CHUNK_SIZE];
            int bytesRead;

            while (true) {
                bytesRead = line.read(buffer, 0, buffer.length);
                graphPanel.repaint();
            }

        } catch (LineUnavailableException ex) {
            ex.printStackTrace();
            statusLabel.setText("Line unavailable");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(AudioVisualizer::new);
    }
}
