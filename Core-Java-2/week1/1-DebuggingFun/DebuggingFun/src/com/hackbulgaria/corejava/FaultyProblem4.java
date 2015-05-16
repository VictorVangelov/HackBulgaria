package com.hackbulgaria.corejava;

public class FaultyProblem4 {
    public static boolean areEqual(Integer e, Integer k) {
        return e.equals(k);
    }

    public static boolean areEqual(float a, float b) {
    	
    	if(Math.abs(a-b) <= 0.00001){    		
    		return true;
    	}
        return a==b;
    }

    /**
     * Return whether there is an index <b>i</b>,
     * such that a[i,a.length] equals b[i, a.length];
     * @param a
     * @param b
     * @return
     */
    public static boolean haveEqualSubstrings(String a, String b) {
        for (int i = 0; i < a.length(); i++) {
            String substringA = a.substring(i, a.length());
            String substringB = b.substring(i, a.length());
            if (substringA.equals(substringB)){
                return true;
            }
        }
        return false;
    }
}
