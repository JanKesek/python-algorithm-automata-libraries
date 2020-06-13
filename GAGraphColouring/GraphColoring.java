import io.jenetics.*;
import io.jenetics.engine.Codecs;
import io.jenetics.engine.Engine;
import io.jenetics.engine.EvolutionStatistics;
import io.jenetics.util.DoubleRange;
import io.jenetics.util.IntRange;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static io.jenetics.engine.EvolutionResult.toBestPhenotype;
import static java.lang.Math.*;

public class GraphColoring {
    public static int[][] adjacencyMatrix;
    private static int fitness(final int[] colors) {
        int conflicts=0;
        List<String> alreadyVisited=new ArrayList<>();
        for(int i=0;i<colors.length;i++) {
            for(int j=0;j<colors.length;j++) {

                if(adjacencyMatrix[i][j]==1) {
                    /*
                    if(!alreadyVisited.contains(Integer.toString(i).concat(Integer.toString(j))) &&
                            !alreadyVisited.contains(Integer.toString(j).concat(Integer.toString(i)))) {
                        alreadyVisited.add(Integer.toString(i).concat(Integer.toString(j)));
                        alreadyVisited.add(Integer.toString(j).concat(Integer.toString(i)));
                        if(colors[i]==colors[j]) conflicts+=1;
                    }
                    */
                    if(colors[i]==colors[j]) conflicts+=1;
                }
            }
        }
        return  conflicts;
    }
    public static String getGraphsHTML(int numberOfVertices) throws Exception {
        Document doc = Jsoup.connect("http://combos.org/gen.php?obj=plantri&n="+numberOfVertices+"&t=0&cm=0&o=false&d=false&graph=4&fmt=1").get();
        String lines[] = doc.body().html().split("\\r?\\n");
        return lines[ThreadLocalRandom.current().nextInt(0, lines.length-5)];
    }
    public static void generateRadomPlanar(int n) {
        adjacencyMatrix=new int[n][n];
        String graphString="";
        try { graphString= getGraphsHTML(n); } catch (Exception e){}
        List<List<Integer>> edges= parseGraphStrig(graphString);
        for(List<Integer> lst : edges) {
            int node=lst.get(0);
            for(int i=1;i<lst.size();i++) {
                adjacencyMatrix[node-1][lst.get(i)-1]=1;
            }
        }
        printAdjacencyMatrix();
    }
    public static void printAdjacencyMatrix() {
        for(int i=0;i<adjacencyMatrix.length;i++) {
            for(int j=0;j<adjacencyMatrix[0].length;j++) {
                System.out.print(" " + adjacencyMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static List<List<Integer>> parseGraphStrig(String graphString) {
        List<String> allMatches = new ArrayList<String>();
        List<List<Integer>> parsedEdges=new ArrayList<List<Integer>>();
        Matcher m = Pattern.compile("([0-9]+\\[.*?\\])")
                .matcher(graphString);
        while (m.find()) {
            allMatches.add(m.group());
        }
        for(String s : allMatches) {
            //System.out.println(s);
            List<Integer> node=new ArrayList<Integer>();
            String[] nodeNeighbors=s.split("\\[");
            node.add(Integer.parseInt(nodeNeighbors[0]));
            String[] neighbors=nodeNeighbors[1].split("]")[0].split(" ");
            for(int i=0;i<neighbors.length;i++) {
                node.add(Integer.parseInt(neighbors[i]));
            }
            parsedEdges.add(node);
        }
        return parsedEdges;
    }
    public static void main(String[] args) {
        int n=11;
        try  { System.setOut(new PrintStream(new FileOutputStream("graph_file.txt"))); } catch (FileNotFoundException e) {}
        generateRadomPlanar(n);
        Engine<IntegerGene, Integer> engine=Engine.builder(GraphColoring::fitness, Codecs.ofVector(IntRange.of(0,3),n))
                .optimize(Optimize.MINIMUM)
                .alterers(new Mutator<>(0.09),new MeanAlterer<>(0.3)).build();
        EvolutionStatistics<Integer,?> statistics=EvolutionStatistics.ofNumber();
        Phenotype<IntegerGene,Integer> best=engine.stream()
                .limit(100000).peek(statistics).collect(toBestPhenotype());
        //System.out.println(statistics);
        //System.out.println(best);
        //System.out.println(best.genotype());
        System.out.println("<==>");
        for(Chromosome ig : best.genotype()) {
             for(Object a : ig) System.out.print(a.toString() + " ");
        }
        //System.out.println("TEST: 3.389125781971881 -> " + fitness(3.389125781971881));
    }

}
