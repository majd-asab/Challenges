class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
    List<Map<Integer,List<Integer>>> array = new ArrayList<Map<Integer,List<Integer>>>();

        for(int i = 0; i < graph.length; i++){
            for(int j = 0; j < graph[i].length; j++) {
                if (i == 0) {
                    List<Integer> ar = new ArrayList<>();
                    ar.add(i);
                    ar.add(graph[i][j]);
                    Map<Integer, List<Integer>> map = new HashMap<>();
                    map.put(graph[i][j], ar);
                    array.add(map);
                }
                else {
                    for(int k = 0; k < array.size(); k++){
                        if (array.get(k).containsKey(i)){
                            List<Integer> ar = new ArrayList<>();
                            Map<Integer, List<Integer>> map = new HashMap<>();
                            // retrieve the path
                            ar = array.get(k).remove(i);
                            // add the new discovered node to the path
                            ar.add(graph[i][j]);
                            // map the the latest node on the path with the key
                            map.put(graph[i][j],ar);
                            // add new path to global array
                            array.add(map);
                            // remove old mapping object
                            array.remove(k);
                        }
                    }
                }
            }
        }

        List<List<Integer>> finArray = new ArrayList<List<Integer>>();
        for(int i = 0; i < array.size();i++){
            for (Map.Entry<Integer, List<Integer>> entry : array.get(i).entrySet()) {
                finArray.add(entry.getValue());
            }

        }
        return finArray;
    }
}
