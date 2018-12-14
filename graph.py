#!/usr/bin/python
couleur = ['yellow','red','blue','green','orange','purple']
from networkx import * 
import pylab as p
graph = {}

# Retourne les arretes du graphes 
def graph_(graph): 
	arete = []
	for noeu,adjacents in graph.items():
		for a in adjacents: 
			if not ((noeu,a) in arete or (a,noeu) in arete):
				arete.append((noeu,a))
	return arete
# affiche les arrets 
def afficher_arete(a):
	print("les arretes sont : ------------------\n")
	resultat = ''
	resultat+= ''.join(' "{}" --- "{}" ,\n'.format(*e) for e in a )
	print resultat
# afficher_arete(graph_({'A': ['B', 'C'],'B': ['A'],'C': ['A']}))
# colors : dictionaire des sommets et leurs couleurs 
def colorer_(graph,nombre_couleurs):
	colors={}
	def differente_color(noeu,color):
		for n in noeu:
			if color==colors.get(n):
				return False
		return True 
	for noeu, adjacents in graph.items():
		found_color = False
		for color in range(nombre_couleurs):
			if(differente_color(adjacents,color)):
				found_color=True
				colors[noeu]=color 
				break
		if not found_color :
			return None 
	print(colors)
	print("\n")
	return colors 

def couleur_graph(graph):
	print("Coloration du graph ---------------------------------------------")
	for nombre in range(1,len(graph)):
		colors = colorer_(graph,nombre)
		if colors: 
			return colors
def list_couleur_utlise(couleur_graphe):
	return(sorted(list(set(couleur_graphe.values()))))
def affiche_list_couleur_utilise(liste):
	print("la liste des couelurs utilisees est : ---------------------------")
	for c in liste :
		print(couleur[c])
	# print("\n")
def list_sommet(graphe):
		print("les sommets du graphe sont ----------------------")
		l = list(graphe.keys())
		print(l)
		return l 
# exemple pour coloriage d'une carte Coloration de la
 # carte de la region Centre-Val de Loire
def dessiner_example(liste_sommet,liste_arrete,graphcouleur):
	# pos = {}
	G=nx.Graph()
	pos={'loir':(1.0,1.2), 
	    'eure':(1.0,2.0), 
	    'loiret':(1.5,1.5), 
	    'cher':(1.5,1.0), 
	    'indre':(1.0,0.5),
	    'indr&loire':(0.5,0.5)}
	labels = {k:k for k in liste_sommet}
		# print(i,j)
	# print(pos)
	for sommet in liste_sommet : 
		# print(sommet )
		# print(couleur[graphcouleur[sommet]])
		nx.draw_networkx_nodes(G,pos,node_size=1300,nodelist=[sommet],label=sommet,node_color=couleur[graphcouleur[sommet]]) 
	nx.draw_networkx_edges(G,pos,liste_arrete,alpha=0.8,width=5) 
	# nx.draw_networkx_labels(G,pos,font_color='black',font_weight='bold',font_size=40)
	p.axis('off')
	p.title("Coloration carte region Centre-Val de Loire")
	p.show()
def exemple_carte(): 
	carte = {'loir': ['eure','loiret','cher','indre','indr&loire'],'eure': ['loir','loiret'],
		'loiret': ['loir','eure','cher'],'cher':['loir','loiret','indre'],'indre': ['loir','cher','indr&loire'],'indr&loire':['loir','indre']}
	# On afficher les arretes correspandant a notre graphe 
	afficher_arete(graph_(carte))
	c = couleur_graph(carte)
	affiche_list_couleur_utilise(list_couleur_utlise(c))
	dessiner_example(list_sommet(carte),graph_(carte),c)




if __name__ == '__main__':


	exemple_carte()