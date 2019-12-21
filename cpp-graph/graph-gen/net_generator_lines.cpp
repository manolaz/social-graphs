#include <iostream>
#include <stdlib.h>
// writing on a text file
#include <fstream>
using namespace std;
void GenRandomGraphs(int NOEdge, int NOVertex)
{
    int i, j, edge[NOEdge][2], count;
    i = 0;
    //Assign random values to the number of vertex and edges
    //of the graph, Using rand().
    while (i < NOEdge)
    {
        edge[i][0] = rand() % NOVertex + 1;
        edge[i][1] = rand() % NOVertex + 1;
        //Print the connections of each vertex, irrespective of
        //the direction.
        if (edge[i][0] == edge[i][1]) continue;
        else
        {
            for (j = 0; j < i; j++)
            {
                if ((edge[i][0] == edge[j][0] &&
                     edge[i][1] == edge[j][1]) ||
                    (edge[i][0] == edge[j][1] &&
                     edge[i][1] == edge[j][0]))
                    i--;
            }
        }
        i++;
    }
    cout << "\nThe generated random graph is: ";

    ofstream myfile("graph.net");
    if (myfile.is_open())
    {
        for (i = 0; i < NOVertex; i++)
        {
            count = 0;
            for (j = 0; j < NOEdge; j++)
            {
                if (edge[j][0] == i + 1)
                {
                    myfile << edge[j][1] << " " << "\n" << i;
                    count++;
                }
                else if (edge[j][1] == i + 1)
                {
                    myfile << edge[j][0] << " ";
                    count++;
                }
                else if (j == NOEdge - 1 && count == 0)
                    myfile << "Isolated Vertex!"; //Print “Isolated vertex” for the vertex having no degree.
            }
        }
        myfile.close();
    }
}
int main()
{
    int i, e, n;
    cout << "Random graph generation: ";
    n = 500 + rand() % 6;
    cout << "\nThe graph has " << n << " vertices";
    e = rand() % ((n * (n - 1)) / 3);
    cout << "\nand has " << e << " edges.";
    GenRandomGraphs(e, n);
}