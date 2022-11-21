A=zeros(64);
for i=1:8
    for j=1:8
        if i==1
            if j==1
                [A(1,2),A(1,9)]=deal(1);
            elseif j==8
                    [A(8,7),A(8,16),A(8,15)]=deal(1);
            else [A(j,j+1),A(j,j-1),A(j,j+8),A(j,j+7)]=deal(1);
            end
        elseif i==8
            if j==1
                [A(57,49),A(57,50),A(57,58)]=deal(1);
            elseif j==8
                [A(64,63),A(64,56)]=deal(1);
            else [A(56+j,55+j),A(56+j,57+j),A(56+j,48+j),A(56+j,49+j)]=deal(1);
            end
        elseif mod(i,2)==0
            if j==1
                [A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j-7),A(8*(i-1)+j,8*(i-1)+j+1),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j+9)]=deal(1);
            elseif j==8
                [A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j-1)]=deal(1);
            else [A(8*(i-1)+j,8*(i-1)+j-1),A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j-7),A(8*(i-1)+j,8*(i-1)+j+1),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j+9)]=deal(1);
            end
        else 
            if j==1
                [A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j+1)]=deal(1);
            elseif j==8
                [A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j-9),A(8*(i-1)+j,8*(i-1)+j-1),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j+7)]=deal(1);
            else [A(8*(i-1)+j,8*(i-1)+j-1),A(8*(i-1)+j,8*(i-1)+j-8),A(8*(i-1)+j,8*(i-1)+j-9),A(8*(i-1)+j,8*(i-1)+j+1),A(8*(i-1)+j,8*(i-1)+j+8),A(8*(i-1)+j,8*(i-1)+j+7)]=deal(1);
            end
        end
    end
end
Graph_2=graph(A);
plot(Graph_2)