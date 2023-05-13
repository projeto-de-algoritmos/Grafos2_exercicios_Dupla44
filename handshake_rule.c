#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// implementar com lista de adjacência

#define lim 4000000
int pa[20000], dist[20000];
int m_nomes[lim];
static int *pq; 
static int N;
static int *qp; 
typedef struct node *link;

struct node {
  int v;
  link next;
};

typedef struct {
  int v, w;
} Edge;

typedef struct {
  int V, E;
  link *adj;
} Graph;

link NEW(int v, link next) {
  link k = malloc(sizeof(link));
  k -> v = v;
  k -> next = next;
  return k;
}

Graph *g_init(int v) {
  Graph *g = malloc(sizeof(g));
  g -> V = v;
  g -> E = 0;
  g -> adj = malloc(v * sizeof(link));

  for(int i = 0; i < v; i++) {
    g -> adj[i] = NULL;
  }

  return g;
}

void g_insert(Graph *g, Edge e) {
  int v = e.v, w = e.w;
  g -> adj[v] = NEW(w, g -> adj[v]);
  g -> adj[w] = NEW(v, g -> adj[w]);
  g -> E++;
}

Edge EDGE(int v, int w) {
  Edge *E = malloc(sizeof(E));
  E -> v = v;
  E -> w = w;
  
  return *E;
}

static void exch( int i, int j) {
  int t;
  t = pq[i]; pq[i] = pq[j]; pq[j] = t;
  qp[pq[i]] = i;
  qp[pq[j]] = j;
}

static void fixUp( int k, int prty[]) {
  while (k > 1 && greater( k/2, k)) {
    exch( k/2, k);
    k = k/2;
  }
}

static void fixDown( int k, int prty[]) { 
  int j;
  while (2*k <= N) { 
    j = 2*k;
    if (j < N && greater( j, j+1)) j++;
    if (!greater( k, j)) break;
    exch( k, j); 
    k = j;
  }
}

void PQinit( int maxN) { 
  pq = malloc( (maxN+1) * sizeof (int));
  qp = malloc( maxN * sizeof (int));
  N = 0; 
}

int PQempty( void) { 
  return N == 0; 
}

void PQinsert(int v, int prty[]) {
  qp[v] = ++N; 
  pq[N] = v; 
  fixUp( N, prty); 
}

int PQdelmin( int prty[]) { 
  exch( 1, N); 
  --N; 
  fixDown( 1, prty); 
  return pq[N+1]; 
}

void PQdec(int w, int prty[]) { 
  fixUp( qp[w], prty); 
}

void PQfree( ) { 
  free( pq);
  free( qp);
}

void fcp(Graph *G, int s, int *pa, int *dist)
{
  int mature[1000];
  for (int v = 0; v < G -> V; ++v)
    pa[v] = -1, mature[v] = 0, dist[v] = __INT_MAX__;
  pa[s] = s, dist[s] = 0;
  PQinit(G -> V);
  for (int v = 0; v < G -> V; ++v)
    PQinsert(v, dist);

  while (!PQempty()) {
    int y = PQdelmin(dist);
    if (dist[y] == __INT_MAX__) break;
    for (link a = G -> adj[y]; a != NULL; a = a -> next) {
      if (mature[a -> v]) continue;
      if (dist[y] + 1 < dist[a -> v]) {
        dist[a -> v] = dist[y] + 1;
        PQdec( a -> v, dist);
        pa[a -> v] = y;
      }
    }
    mature[y] = 1;
  }
  PQfree( );
}

void print_lista(Graph *g) {
  for(int i = 0; i < g->V; i++) {
    for(link a = g->adj[i]; a != NULL; a = a -> next) {
      printf("%d", a->v);
      if(a -> next != NULL) printf(" -> ");
    }
    printf("\n");
  }
}

#define debug 0

unsigned convert (char *s) {
  unsigned long long h = 0;
  for (int i = 0; s[i] != '\0'; i++) 
    h = h * 1000039 + s[i];
  return h;
}

int main() {
  char nome[26];
  char fp[26], lp[26], nome1[26], nome2[26];
  int n, m;

  scanf(" %s %s", fp, lp);
  scanf("%d %d", &n, &m);
  Graph *g = g_init(n);

  for(int i = 0; i < n; i++) {
    scanf(" %s", nome);
    m_nomes[convert(nome) % lim] = i;
    g -> adj[i] = NEW(i, g -> adj[i]);
  }

  for(int i = 0; i < m; i++) {
    scanf(" %s %s", nome1, nome2);
    g_insert(g, EDGE(m_nomes[convert(nome1) % lim], m_nomes[convert(nome2) % lim]));
  }

  if(debug) print_lista(g);

  fcp(g, m_nomes[convert(fp) % lim], pa, dist);

  int fim = dist[m_nomes[convert(lp) % lim]];
  printf("%d\n", fim != __INT_MAX__ ? fim : -1);  

  return 0;
}