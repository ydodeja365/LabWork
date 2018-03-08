import java.util.Scanner;
class equation{
	/*For calculating Determinant of the Matrix */
float determinant(float a[25][25], float k)
{
  float s = 1, det = 0, b[25][25];
  int i, j, m, n, c;
  if (k == 1)  
  {
     	return (a[0][0]);
  }
  else
 {
    det = 0;
     for (c = 0; c < k; c++)
       {
        m = 0;
        n = 0;
        for (i = 0;i < k; i++)
        {
           for (j = 0 ;j < k; j++)
           {
                b[i][j] = 0;
                if (i != 0 && j != c)
                {
                  b[m][n] = a[i][j];
                  if (n < (k - 2))
                  n++;
                  else
                 {
                    n = 0;
                    m++;
                 }
                }
               }
             }
          det = det + s * (a[0][c] * determinant(b, k - 1));
          s = -1 * s;
          }
    }
    return (det);
}

float[][] cofactor(float num[25][25], float f)

{

 float b[25][25], fac[25][25];

 int p, q, m, n, i, j;

 for (q = 0;q < f; q++)

 {

   for (p = 0;p < f; p++)

    {

     m = 0;

     n = 0;

     for (i = 0;i < f; i++)

     {

       for (j = 0;j < f; j++)

        {

          if (i != q && j != p)

          {

            b[m][n] = num[i][j];

            if (n < (f - 2))

             n++;

            else

             {

               n = 0;

               m++;

               }

            }

        }

      }

      fac[q][p] = pow(-1, q + p) * determinant(b, f - 1);

    }

  }

  return transpose(num, fac, f);

}
/*Finding transpose of matrix*/ 
float[][] transpose(float num[25][25], float fac[25][25], float r)
{
  int i, j;
  float b[25][25], inverse[25][25], d;
  for (i = 0;i < r; i++)
    {
     for (j = 0;j < r; j++)
       {
         b[i][j] = fac[j][i];
        }
    }
  d = determinant(num, r);
  for (i = 0;i < r; i++)

    {

     for (j = 0;j < r; j++)

       {

        inverse[i][j] = b[i][j] / d;

        }

    }
return inverse;
}
public static float[][] multiplyMatrices(float[][] firstMatrix, float[][] secondMatrix, int r1, int c1, int c2){
        float[][] product = new float[r1][c2];
        for(int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                for (int k = 0; k < c1; k++) {
                    product[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
                }
            }
        }

        return product;
    }
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number of variables:");
		int num_var = s.nextInt();
		if(n>0)
		{
			float coeff[][] = new float [num_var][num_var];
			float consta[][] = new float [num_var][1];
			System.out.println("Enter coefficients of variable in every equation:");
			for (int i=0;i<num_var;i++)
			{
				for(int j=0;j<num_var;j++)
					coeff[i][i] = s.nextFloat();
			}
			System.out.println("Enter the constants:");
			for (int i=0;i<num_var;i++) 
			{
				consta[i][0] = s.nextFloat();
			}
			  d = determinant(a, k);
			if (d == 0)
  				System.out.print("\nInverse of Entered Matrix is not possible\n");
  			else
  			{
				float[][] inv = cofactor(coeff);
				float answer[] = multiplyMatrices(consta,inv,num_var,num_var,1);
				System.out.println("Solution set is [ ");
				for(int i=0;i<num_var;i++)
					System.out.print(Float.toString(answer[i]));
				System.out.print("]\n");
			}
		}
	}
}