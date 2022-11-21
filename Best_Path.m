tic
flags=zeros(3,10);
str=zeros(1,10);
date=1;
node=[1,0,0,0,0,0,0,0,0,0,0];
money=zeros(1,11);
food=zeros(1,11);
water=zeros(1,11);
max_money=-1e10;
while date~=0
    if date>10 && node(date)<6
        str(date)=0;
        [money(date),food(date),water(date)]=deal(0);
        date=date-1;
        if date==0
            break
        end
        node(date+1)=0;
    elseif node(date)==6
        if max_money<money(date)+5*food(date)+10*water(date)
            max_money=money(date)+5*food(date)+10*water(date);
            str0=str;
        end
        str(date)=0;
        [money(date),food(date),water(date)]=deal(0);
        node(date)=0;
        date=date-1;
        if date==0
            break
        end
    elseif node(date)~=4
        for strategy=0:1
            if flags(strategy+1,date)==0
                flags(strategy+1,date)=1;
                if strategy==1
                    node(date+1)=node(date)+1;
                else
                    node(date+1)=node(date);
                end
                [money(date+1),food(date+1),water(date+1)]=stchange(money(date),food(date),water(date),strategy,date);
                str(date)=strategy;
                date=date+1;
                break
            end
            if flags(1,date)==1 && flags(2,date)==1
                str(date)=0;
                node(date)=0;
                [money(date),food(date),water(date)]=deal(0);
                flags(:,date)=0;
                date=date-1;
                if date==0
                    break
                end
            end
        end
    elseif node(date)==4
        if flags(1,date)==1 && flags(3,date)==1 && flags(2,date)==0
            str(date)=0;
            node(date)=0;
            [money(date),food(date),water(date)]=deal(0);
            flags(:,date)=0;
            date=date-1;
            if date==0
                break
            end
        end
        for strategy=0:2
            if flags(strategy+1,date)==0
                flags(strategy+1,date)=1;
                if flags(:,date)==1
                    flags(2,date)=0;
                end
                if strategy==1
                    node(date+1)=node(date)+1;
                else
                    node(date+1)=node(date);
                end
                [money(date+1),food(date+1),water(date+1)]=stchange(money(date),food(date),water(date),strategy,date);
                str(date)=strategy;
                date=date+1;
                break
            end
        end
    end
end
toc