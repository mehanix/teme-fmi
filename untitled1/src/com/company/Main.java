package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

import static com.company.Problema.solve;

public class Main {


    public static void main(String[] args) {
        Problema.readInput();
        solve();
    }

}

class Problema {

    static private int N, M; // coloane linii
    static private int[][] insula;
    static private ArrayList<Integer> perimetre = new ArrayList<>();
    static private int[] posx = {0, 0, 1, -1};
    static private int[] posy = {1, -1, 0, 0};

    static void readInput() {
        MyScanner sc = new MyScanner();
        M = sc.nextInt();
        N = sc.nextInt();
        insula = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                insula[i][j] = sc.nextInt();
            }
        }
    }

    static boolean inBounds(int x, int y) {
        if (x < 0 || x >= M || y < 0 || y >= N)
            return false;
        return true;
    }

    static void fill(int noInsula, int x, int y) {
        if (x < 0 || x >= M || y < 0 || y >= N)
            return;
        if (insula[x][y] == 2)
            return;
        if (insula[x][y] == -1) {
            return;
        }

        insula[x][y] = 2;
        if (x == 1 && y == 2)
            System.out.println("in cautat");
        boolean margine = false;
        for (int i = 0; i < 3; i++) {
            if (inBounds(x+posx[i], y + posy[i]))
                if ( insula[x+posx[i]][y + posy[i]] == -1){
                    margine = true;
                }
        }
        if (margine) {
            System.out.println("MARGINEEE " + x +' ' + y);
            perimetre.set(noInsula, perimetre.get(noInsula) + 1);
        }
        fill(noInsula, x + 1, y);
        fill(noInsula, x - 1, y);
        fill(noInsula, x, y + 1);
        fill(noInsula, x, y - 1);
    }

    static void solve() {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (insula[i][j] == 1) {
                    perimetre.add(perimetre.size(), 0);
                    fill(perimetre.size() - 1, i, j);

                }
            }
        }

        if (perimetre.size() == 0) {
            System.out.println("-1");
        } else {
            perimetre.sort((i1, i2) -> i2 - i1);
            for (int i = 0; i < perimetre.size(); i++) {
                System.out.println(perimetre.get(i));
            }
        }
    }


    static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}