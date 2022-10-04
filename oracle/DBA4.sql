--��ǰ���̺�� ��ǰ�з����̺��� ��ǰ�з��ڵ尡 'P101'�� �Ϳ� ����
--��ǰ�з��ڵ�(��ǰ���̺� �ִ� Į��), ��ǰ��, ��ǰ�з����� ��ȸ�� �ּ���.
--������ ��ǰ���̵�� ��������...

SELECT prod_lgu, prod_name, lprod_nm
from prod, lprod
where prod_lgu = lprod_gu
and prod_lgu = 'P101'
order by prod_name desc;
--
select prod_lgu, prod_name, lprod_nm
from prod inner join lprod
on(prod_lgu = lprod_gu and prod_lgu = 'P101')
order by prod_name desc;

--������ ȸ���� ������ ��ǰ�� ����
--�ŷ�ó ������ Ȯ���Ϸ��� �մϴ�.
--�ŷ�ó�ڵ�, �ŷ�ó��, ȸ����������(���� or  ��õ...)��ȸ
--�� ��ǰ�з��� �߿� ĳ�־� �ܾ ���Ե� ��ǰ�� ���ؼ���...
select buyer_id, buyer_name, substr(mem_add1,1,2)
from buyer,member,cart,prod,lprod
where buyer_id=prod_buyer
and lprod_gu =prod_lgu
and cart_prod=prod_id
and cart_member = mem_id
and mem_name = '������'
and lprod_nm like '%ĳ�־�%';

--��ǰ�з��� '����'�� ���Ե� ��ǰ�� ������ ȸ�� ��ȸ�ϱ�
--ȸ�����̵�, ȸ���̸�, ��ǰ�з��� ��ȸ�ϱ�.
--��, ��ǰ�� �Ｚ���ڰ� ���Ե� ��ǰ�� ������ ȸ����...
--ȸ���� ��̰� ������ ȸ��
select mem_id, mem_name, lprod_nm
from member,cart,prod,lprod
where mem_id=cart_member
    and mem_like ='����'
and cart_prod =prod_id
    and prod_name like '�Ｚ����%'
and prod_lgu =lprod_gu
    and lprod_nm like '����%'
;

--��ǰ�з����̺�� ��ǰ���̺�� �ŷ�ó���̺�� ��ٱ��� ���̺� ���..
--��ǰ�з��ڵ尡 'p101'�� ���� ��ȸ
--�׸���, ������ ��ǰ�з����� �������� ��������,
--            ��ǰ���̵� �������� �������� �ϼ���..
--��ǰ�з���, ��ǰ���̵�, ��ǰ�ǸŰ�, �ŷ�ó�����, ȸ�����̵�,
--�ֹ������� ��ȸ..
select lprod_nm, prod_name, prod_sale, mem_id,cart_qty
from lprod, prod, buyer, cart, member
where lprod_gu = prod_lgu
and lprod_gu = 'P101'
and prod_buyer = buyer_id
and prod_id = cart_prod
and cart_member = mem_id
order by prod_id asc , lprod_nm desc;

select lprod_nm, prod_name, prod_sale, mem_id,cart_qty
from lprod inner join prod
on(lprod_gu = prod_lgu and lprod_gu = 'P101')
 inner join buyer 
on(prod_buyer = buyer_id)
 inner join cart 
on(prod_id = cart_prod)
 inner join member
on(cart_member = mem_id)
order by prod_id asc , lprod_nm desc;

--��ǰ�ڵ庰 ���ż����� ���� �ִ�, �ּҰ�,��հ�,�հ�,���� ��ȸ�ϱ�,
--��, ��ǰ�� �Ｚ�� ���Ե� ��ǰ�� ������ ȸ���� ���ؼ���
--��ȸ�÷� ��ǰ�ڵ�, �ִ��, �ּҰ�, ��հ�, �հ�, ����
select prod_id, max(cart_qty)as max, min(cart_qty)as min,
    round(avg(cart_qty),2)as avg, sum(cart_qty)as sum, count(cart_qty) as count 

from prod, cart
where prod_id = cart_prod

and  prod_name like '�Ｚ%'
group by prod_id
;

--�ŷ�ó�ڵ� �� ��ǰ�з��ڵ庰��,
---�ǸŰ��� ���� �ְ�, �ּ�, �ڷ��, ���, �հ踦 ��ȸ�� �ּ���.
--��ȸ�ä���, �ŷ�ó�ڵ�, �ŷ�ó��, ��ǰ�з��ڵ�, ��ǰ�з���,
            --�ǸŰ��� ���� �ְ�, �ּ�, �ڷ��, ���, �ղ�
--������ ����� �������� ��������
--��, �ǸŰ��� ����� 100�̻��� ��
select buyer_id, prod_name,lprod_gu,lprod_nm,
max(prod_sale), min(prod_sale), count(prod_sale), avg(prod_sale) as avg, sum(prod_sale)
from buyer,lprod, prod
where buyer_lgu = lprod_gu
and lprod_gu = prod_lgu
group by buyer_id, prod_name, lprod_gu, lprod_nm
having avg(prod_sale) >=100
order by avg desc;


--�ŷ�ó���� group ��� ���Աݾ��� ���� �˻��ϰ��� �մϴ�...
--������ ��ǰ�԰����̺��� 2005�⵵ 1���� ��������(�԰�����)�ΰ͵�...
--���Աݾ� = ���� ���� * ���Աݾ�..
--��ȸ�÷� : �ŷ�ó�ڵ�, �ŷ�ó��, ���Աݾ��� �� 
--(���Աݾ��� ���� null�� ��� 0���� ��ȸ)
--������ �ŷ�ó �ڵ� �� �ŷ�ó���� �������� ��������

select buyer_id, buyer_name , nvl(sum(buy_qty * buy_cost),0)as buy_cost
from buyer, prod,buyprod
where buyer_id = prod_buyer
and prod_id = buy_prod
and buy_date between '05/01/01' and '05/01/31'
group by buyer_id, buyer_name
order by buyer_id desc,buyer_name desc;

select substr(buy_date,1,5) 
from buyprod;

--�ŷ�ó���� group ��� ���Աݾ��� ���� ����Ͽ�
--���Աݾ��� ���� 1õ������ �̻��� ��ǰ�ڵ�, ��ǰ�� �˻��ϰ��� �մϴ�..
--������ ��ǰ�԰����̺��� 2005�⵵ 1���� ��������(�԰�����)�ΰ͵�...
--���Աݾ� = ���Լ���* ���Աݾ�..
--(���Աݾ��� ���� null�� ��� 0���� ��ȸ)
--��ȸ�÷� : ��ǰ�ڵ� , ��ǰ��
--������ ��ǰ���� �������� ��������

select prod_id, prod_name
from prod, buyprod
where prod_id = buy_prod
and buy_date between '05/01/01' and '05/01/31'
having sum(nvl(buy_qty * buy_cost,0)) >=10000000
group by prod_id,prod_name
order by prod_name asc;