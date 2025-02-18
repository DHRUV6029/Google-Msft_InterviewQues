import java.util.*;;

class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
public class App {
    public static void main(String[] args) throws Exception {
        Node head = new Node(1);
        head.next = head;

        var map = buildSelfBalancedBst(head);
        addNode(map, 1, head);  // Head remains same
        addNode(map,0, head);

        System.out.println("fewfew");
    }

    public static TreeMap<Integer, Node> buildSelfBalancedBst(Node head) {
        TreeMap<Integer, Node> treeMap = new TreeMap<>();
        treeMap.put(head.val, head);
        Node cur = head.next;
        
        while (cur != null && cur != head) {
            treeMap.put(cur.val, cur);
            cur = cur.next;
        }
        return treeMap;
    }

    public static void addNode(TreeMap<Integer, Node> treeMap, int target, Node head) {
        Node newNode = new Node(target);

        var floorEntry = treeMap.floorEntry(target);
        var ceilingEntry = treeMap.ceilingEntry(target);

        treeMap.put(target, newNode);
        
        if(ceilingEntry != null && floorEntry != null){
            newNode.next = ceilingEntry.getValue();
            floorEntry.getValue().next = newNode;
        } else if (floorEntry != null && ceilingEntry == null){
            floorEntry.getValue().next = newNode;
            newNode.next = floorEntry.getValue();
        }else if (floorEntry == null && ceilingEntry != null){
            newNode.next = ceilingEntry.getValue();
            ceilingEntry.getValue().next = newNode;
        }
        
    }

}
