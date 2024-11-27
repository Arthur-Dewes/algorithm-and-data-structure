
import java.util.NoSuchElementException;

public class BinaryTreeOfInteger {

    private static final class Node {

        public Node father;
        public Node left;
        public Node right;
        private Integer element;

        public Node(Integer element) {
            father = null;
            left = null;
            right = null;
            this.element = element;
        }
    }

    private int count;
    private Node root;

    public BinaryTreeOfInteger() {
        count = 0;
        root = null;
    }

    public void clear() {
        count = 0;
        root = null;
    }

    public boolean isEmpty() {
        return (root == null);
    }

    public int size() {
        return count;
    }

    public Integer getRoot() {
        if (isEmpty()) {
            throw new EmptyTreeException();
        }
        return root.element;
    }
    
    // Metodo privado que procura por element a partir de target
    // e retorna a referencia para o nodo no qual element esta
    // armazenado. Retorna null se nao encontrar element.
    private Node searchNodeRef(Integer element, Node target) {
        if ( target == null)
            return null;

        if (element.equals(target.element))
            return target; 

        Node aux = searchNodeRef(element, target.left);

        if (aux == null)
            aux = searchNodeRef(element, target.right);

        return aux;
    }

    public boolean contains(Integer element) {
        Node nAux = searchNodeRef(element, root);
        return (nAux != null);
    }

    public Integer getParent(Integer element) {
        Node n = this.searchNodeRef(element, root);
        if (n == null) {
            return null;
        } else if (n.father==null) {
            return null;
        }else {
            return n.father.element;
        }
    }

    public void setRoot(Integer element) {
        if (root != null){
            root.element = element;
        }
    }

    public boolean addRoot(Integer element) {
        if (root != null) // se a arvore nao estiver vazia
            return false;
        root = new Node(element);
        count++;
        return true;
    }

    public boolean addLeft(Integer element, Integer elemFather) {
        Node aux = searchNodeRef(elemFather,root);

        if (aux == null)
            return false;

        if (aux.left != null)
            return false;

        Node n = new Node(element);
        n.father = aux;
        aux.left = n;
        count++;
        return true;
    }

    public boolean addRight(Integer element, Integer elemFather) {
        Node aux = searchNodeRef(elemFather,root);

        if (aux == null)
            return false;

        if (aux.right != null)
            return false;

        Node n = new Node(element);
        n.father = aux;
        aux.right = n;
        count++;
        return true;
    }

    private int countNodes(Node n) {
        if (n==null)
            return 0;
        return 1 + countNodes(n.left) + countNodes(n.right);
    }

    public boolean remove(Integer element) {
        Node nodeToRemove = searchNodeRef(element, root);
    
        if (nodeToRemove == null) {
            return false; // Elemento não encontrado
        }
    
        // Caso 1: Nó é uma folha
        if (nodeToRemove.left == null && nodeToRemove.right == null) {
            if (nodeToRemove == root) {
                root = null; // Se for a raiz e único elemento
            } else {
                if (nodeToRemove.father.left == nodeToRemove) {
                    nodeToRemove.father.left = null;
                } else {
                    nodeToRemove.father.right = null;
                }
            }
        }
        // Caso 2: Nó tem apenas um filho (esquerdo ou direito)
        else if (nodeToRemove.left == null || nodeToRemove.right == null) {
            Node child = (nodeToRemove.left != null) ? nodeToRemove.left : nodeToRemove.right;
    
            if (nodeToRemove == root) {
                root = child; // Se for a raiz
            } else {
                if (nodeToRemove.father.left == nodeToRemove) {
                    nodeToRemove.father.left = child;
                } else {
                    nodeToRemove.father.right = child;
                }
            }
            child.father = nodeToRemove.father;
        }
        // Caso 3: Nó tem dois filhos
        else {
            Node successor = findMin(nodeToRemove.right);
            nodeToRemove.element = successor.element; // Substitui o valor pelo sucessor
            remove(successor.element); // Remove o sucessor
        }
    
        count--;
        return true;
    }
    
    // Método auxiliar para encontrar o menor nó na subárvore
    private Node findMin(Node node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    public LinkedListOfInteger positionsPre() {
        LinkedListOfInteger lista = new LinkedListOfInteger();
        positionsPreAux(root, lista);
        return lista;
    }

    private void positionsPreAux(Node n, LinkedListOfInteger lista) {
        if (n != null) {
            lista.add(n.element);
            positionsPreAux(n.left,lista);
            positionsPreAux(n.right,lista);
        }
    }
}
