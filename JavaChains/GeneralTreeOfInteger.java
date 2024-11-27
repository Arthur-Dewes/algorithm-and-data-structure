import java.util.LinkedList;

public class GeneralTreeOfInteger {

    private class Node {
        public Node father;
        public Integer element;
        public LinkedList<Node> subtrees;

        public Node(Integer element) {
            father = null;
            this.element = element;
            subtrees = new LinkedList<>();
        }

        private void addSubtree(Node n) {
            n.father = this;
            subtrees.add(n);
        }

        private boolean removeSubtree(Node n) {
            n.father = null;
            return subtrees.remove(n);
        }

        public Node getSubtree(int i) {
            if ((i < 0) || (i >= subtrees.size())) {
                throw new IndexOutOfBoundsException();
            }
            return subtrees.get(i);
        }

        public int getSubtreesSize() {
            return subtrees.size();
        }
    }

    private Node root;
    private int count;

    public GeneralTreeOfInteger() {
        root = null;
        count = 0;
    }

    public int size() {
        return count;
    }

    private Node searchNodeRef(Integer elem, Node n) {
        if (n == null)
            return null;

        if (elem.equals(n.element))
            return n;

        Node aux = null;
        for (int i = 0; i < n.getSubtreesSize(); i++) {
            aux = searchNodeRef(elem, n.getSubtree(i));
            if (aux != null)
                return aux;
        }
        return aux;
    }

    public boolean add(Integer elem, Integer elemFather) {
        Node n = new Node(elem);

        if (elemFather == null) {
            if (root != null) {
                root.father = n;
                n.addSubtree(root);
            }
            root = n;
            count++;
            return true;
        } else {
            Node aux = searchNodeRef(elemFather, root);
            if (aux != null) {
                n.father = aux;
                aux.addSubtree(n);
                count++;
                return true;
            }
        }
        return false;
    }

    public boolean contains(Integer elem) {
        Node aux = searchNodeRef(elem, root);
        return (aux != null);
    }

    public LinkedList<Integer> positionsWidth() {
        LinkedList<Integer> lista = new LinkedList<>();
        if (root != null) {
            Queue<Node> fila = new Queue<>();
            fila.enqueue(root);
            while (!fila.isEmpty()) {
                Node aux = fila.dequeue();
                lista.add(aux.element);
                for (int i = 0; i < aux.getSubtreesSize(); i++) {
                    fila.enqueue(aux.getSubtree(i));
                }
            }
        }
        return lista;
    }

    public LinkedList<Integer> positionsPre() {
        LinkedList<Integer> lista = new LinkedList<>();
        positionsPreAux(root, lista);
        return lista;
    }

    private void positionsPreAux(Node n, LinkedList<Integer> lista) {
        if (n != null) {
            lista.add(n.element);
            for (int i = 0; i < n.getSubtreesSize(); i++) {
                positionsPreAux(n.getSubtree(i), lista);
            }
        }
    }

    public LinkedList<Integer> positionsPos() {
        LinkedList<Integer> lista = new LinkedList<>();
        positionsPosAux(root, lista);
        return lista;
    }

    private void positionsPosAux(Node n, LinkedList<Integer> lista) {
        if (n != null) {
            for (int i = 0; i < n.getSubtreesSize(); i++) {
                positionsPosAux(n.getSubtree(i), lista);
            }
            lista.add(n.element);
        }
    }

    public int level(Integer element) {// implementado
        Node node = searchNodeRef(element, root);
        if (node == null) {
            return -1; // Elemento não encontrado
        }

        int level = 0;
        while (node.father != null) { // Subir até a raiz
            node = node.father;
            level++;
        }
        return level;
    }

    public boolean removeBranch(Integer element) {//implementado
        Node node = searchNodeRef(element, root);
        if (node == null) {
            return false;
        }

        if (node == root) {
            root = null;
            count = 0;
            return true;
        }

        Node father = node.father;
        if (father != null) {
            father.removeSubtree(node); // Remove o nó da lista de filhos do pai
            // Subtrai o número de nós na subárvore removida, calcular o número total de nós na subárvore 
            //cuja raiz é o nó node
            count -= countNodes(node); 
            return true;
        }

        return false;
    }

    private int countNodes(Node n) {//implementado
        if (n == null) {
            return 0;
        }
    
        int total = 1;
        for (int i = 0; i < n.getSubtreesSize(); i++) {
            total += countNodes(n.getSubtree(i));
        }
        return total;
    }

    public void geraNodosDOT(Node n) {
        System.out.println("node [shape = circle];\n");

        LinkedList<Integer> L = new LinkedList<>();
        L = positionsPre();

        for (int i = 0; i < L.size(); i++) {
            System.out.println("node" + L.get(i) + " [label = \"" + L.get(i) + "\"]");
        }
    }

    public void geraConexoesDOT(Node n) {
        for (int i = 0; i < n.getSubtreesSize(); i++) {
            Node aux = n.getSubtree(i);
            System.out.println("node" + n.element + " -> " + "node" + aux.element + ";");
            geraConexoesDOT(aux);
        }
    }

    public void geraDOT() {
        if (root != null) {
            System.out.println("digraph g { \n");
            geraNodosDOT(root);
            geraConexoesDOT(root);
            System.out.println("}\n");
        }
    }
}
