
{
    int m,n,i,j,k,obj1,obj2;
    int distance;
    printf("Enter no of objects and features:\n");
    scanf("%d %d",&m,&n);
    char datamatrix[m][n];
    double dist[m][m];
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("Enter feature %d for object %d:",j+1,i+1);
            scanf("%s",&datamatrix[i][j]);
        }
    }
    printf("The data_matrix is:\n");
    for(i=0;i<m;i++)
    {

        for(j=0;j<n;j++)
        {
            printf("%c  ",datamatrix[i][j]);
        }
        printf("\n");
    }
    for(i=0;i<m;i++)
    {

        for(j=0;j<m;j++)
        {
            distance=0;
            for(k=0;k<n;k++)
            {
                if(datamatrix[i][k]==datamatrix[j][k])
                distance=distance+1;
            }
            dist[i][j]=(n-distance)/n;
        }
    }
    printf("Distance Matrix is:\n\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%lf  ",dist[i][j]);
        }
        printf("\n");
    }
    distance=10000000;
    for(i=0;i<m;i++)
    {
        for(j=0;j<m;j++)
        {
            if(i==j)
                continue;
            if(distance>dist[i][j])
            {
                distance=dist[i][j];
                obj1=i;
                obj2=j;
            }
        }
    }
    printf("\n\n");
    printf("the most alike objects are %d %d\n",obj1+1,obj2+1);
    printf("distance is:%lf\n",distance);
    return 0;

}