
# Projeto 1

**Deadline:** 18/11/2022

**Delta:** 16/12/2022

## Atenção

**Não haverá** mais projeto 2.

**Aguardem** o enunciado do projeto delta.

As rubricas do projeto foram alteradas:
- Basta dar a volta e fazer o slalom para tirar C (independente da quantidade de integrantes do grupo)
- As rubricas tiveram seus conceitos aumentados
- Todos os grupos terão direito ao projeto Delta caso não atinjam o conceito C.

Para maiores informações, leiam atentamente a rubrica de cada conceito.

## Cenário

O cenário do projeto é a pista do laboratório 404, incluindo os elementos apresentados na figura abaixo

<img src="trevo.png"></img>

O mesmo cenário está disponível no simulador, através do comando:

    roslaunch my_simulation trevo.launch

Para habilitar o controle da garra executar:

	roslaunch mybot_description mybot_control2.launch 	


## Missão:

O robô deverá percorrer as duas alças do trevo, fazendo um tour de recohecimento do terreno e mapeando as posições das bases, ou seja, das caixas contendo as imagens reconhecíveis através da MobileNet, usando as informações de odometria e do lidar e/ou da Intel Realsense. Então deverá ir até a reserva de creepers e pegar um creeper com ID e cor específicas, voltar à pista e levar até a base.

O tour e a missão de levar o creeper até a base podem ser realizadas concomitantemente ou sequencialmente, a critério do grupo.

No percurso ao longo da pista o robô deve realizar um slalom passando entre as caixas azul e vermelhas, continuando a seguir a pista depois disso

O projeto deve ser realizado na pista física da sala de aula, de forma que
o simulador é uma ferramenta para testar a implementação.

## Iniciando o projeto

Todos os integrantes do seu grupo deverão aceitar a tarefa no Github classroom que se encontra neste link:
https://classroom.github.com/a/kJ8RlsZQ


Veja que não há código de template, e portanto seu grupo deverá criar o projeto ROS. Para criar a pasta do projeto, siga as instruções em:
https://github.com/Insper/robot22.2/blob/master/guides/projeto_rospython.md


Em especial atenção ao nome da pasta do repositório do projeto, como está especificado em:
https://github.com/Insper/robot22.2/blob/master/guides/projeto_rospython.md#usando-o-github-classroom


## Rubricas

**Conceito C - Todos os grupos**

O robô percorre as duas alças da pista, parando onde começou, usando
a odometria para saber de onde saiu e fazendo o slalom. É preciso gravar todo o circuito,  que deve ser percorrido em mendos de 15 min. O video de demonstração deve correr ininterruptamente.

**Conceito B - 3 integrantes**
**Conceito C+ - 4 integrantes**

Robô é capaz de percorrer toda a pista, fazendo o *slalom*, parando onde começou. Durante a volta ou depois de dar volta, deve procurar e se chocar contra um creeper da cor certa e ID corretos, voltando depois à pista. A cor e o ID do creeper deve ser escolhida como um parâmetro do programa, ou seja, deve funcionar para qualquer cor e ID pedidos (desde a dupla seja válida).

É preciso gravar todo o circuito, que deve ser percorrido em menos de 20 min. O video deve demonstrar um dos [goals](#objetivos-da-missão) junto com a volta na pista. Os demais [goals](#objetivos-da-missão) podem ser filmados só no momento de derrubar o creeper.

**Conceito B+ - 3 integrantes**
**Conceito B - 4 integrantes**

Robô é capaz de percorer toda a pista, fazendo o slalom, parando onde começou. Depois, deve procurar e "encostar" em um creeper da cor certa e ID corretos, voltando depois à pista. A cor e o ID do creeper deve ser escolhida como um parâmetro do programa, ou seja, deve funcionar para qualquer cor e ID pedidos (desde a dupla seja válida). É preciso gravar todo o circuito, que deve ser percorrido em mendos de 20 min.

Encostar no creeper significa, especificamente: chegar bem perto do creeper com a garra abaixada, e então parar o robô e levantar a garra e encostar nele ou derrubá-lo.

É preciso gravar todo o circuito, que deve ser percorrido em mendos de 20 min. O video deve demonstrar um dos [goals](#objetivos-da-missão) junto com a volta na pista. Os demais [goals](#objetivos-da-missão) podem ser filmados só no momento de derrubar o creeper.

Para atingir este conceito, também é necessário demonstrar o trabalho em equipe, com commits equilibrados de todos os integrantes. Isso vale para todos os conceitos superiores também. 


**Conceito A - 3 integrantes** 
**Conceito B+ - 4 integrantes**

O robô deve percorrer toda a pista, parando onde começou, e no meio do caminho pega o creeper da cor e ID corretos com a garra e volta para a pista. 

A cor e o ID devem ser parâmetros do programa, ou seja, ele deve funcionar para qualquer valor de cor e ID.  

O código tem que estar bem modularizado em comportamentos, e cada função/método deve estar documentada explicando de forma resumida o que faz, como no exemplo abaixo:

```python

def soma(a,b):
	'''
	Retorna a soma de a e b, onde a e b são números reais
	'''
  	return a + b
```

É preciso gravar todo o circuito, que deve ser percorrido em mendos de 20 min.O video deve demonstrar um dos [goals](#objetivos-da-missão) junto com a volta na pista. Os demais [goals](#objetivos-da-missão) podem ser filmados só no momento de derrubar o creeper.


**Conceito A+ - 3 integrantes** 
**Conceito A - 4 integrantes** 

Além dos itens do conceito A, o robô deve deixar o creeper na na base certa e completar mais uma volta na pista.
A base também deve ser fornecida como parâmetro do projeto. 

É preciso gravar todo o circuito, que deve ser percorrido em mendos de 20 min.O video deve demonstrar um dos [goals](#objetivos-da-missão) junto com a volta na pista. Os demais [goals](#objetivos-da-missão) podem ser filmados só no momento de derrubar o creeper.

**Conceito A+ - 4 integrantes**

Itens do conceito B+ mais o uso de classes e objetos Python    

Só pode ter sleep dentro do `while` principal. 

Fazer um dentre os quatro *especiais*:
* Fazer um controle proporcional para manter o robô na pista, alinhar pelo creeper e pela base.
* Usar o ponto de fuga ou o regressão linear da libha de centro para ajudar na centralização do robô (quando cabível)
* Mapear os Arucos da pista e dos creepers usando o modo 3D e odometria.
* Estruturar o programa com pelo menos um node ROS prestando serviço para o outro.

### Grupos de 4 pessoas 

Os grupos de 4 pessoas terão sempre um conceito deslocado em relacão aos de 3 pessoas.

Para obter A+ num grupo de 4, é necessário  fazer os 4 especiais.

Assim, o necessário para conceito B em grupos de 3 representa o conceito C+ em grupos de 4.

# Objetivos da missão 

### Exemplos de objetivos da missão (devem ser filmados): 

Cores válidas do creeper: `blue`, `green`, `pink`.

Estações válidas: `cat`, `car`, `horse` e `bird`

Os objetivos abaixo são exemplos de objetivos possíveis, e que devem ser filmados para fins de demonstração.  O seu robô deve ser capaz de realizar *qualquer* objetivo. 

O primeiro objetivo deve ser gravado junto com a volta do robo na pista, sem cortes. Os demais objetivos podem ser filmados sem o robo precisar dar outra volta na pista.


```python
goal1 = ("blue", 11, "bird")

goal2 = ("green", 11, "car")

goal3 = ("red", 21, "horse")
```


Por exemplo, o objetivo `("blue", 22, "bird")` significa *Encontre o creeper azul de ID 22 e o traga até a caixa com figura de pássaro*. 


# Instruções

Comandos para atualizar os repositório
```bash
    cd ~/catkin_ws/src/mybot_description
    git pull
    cd ~/catkin_ws/src/my_simulation
    git pull
    cd ~/catkin_ws/src/robot22.2
    git pull
```

Para executar:

	roslaunch my_simulation trevo.launch

Para habilitar o controle da garra executar:

	roslaunch mybot_description mybot_control2.launch 	


Como atividade inicial, sugiro que tente fazer o robô *seguir a pista* . Você pode se basear em sua Atividade 3, ou ainda desenvolver uma abordagem baseada em centro de massa da linha amarela, como [encontrada neste link](https://github.com/osrf/rosbook/blob/master/followbot/follower_color_filter.py)


# Exemplo do ARUCO 

Exemplo de como interpretar os markers ARUCO [./aruco/aruco.ipynb](./aruco/aruco.ipynb)

Exemplo de como programar usando os markers ARUCO em 3D 
[https://github.com/Insper/robot22.2/blob/master/projeto/aruco/aruco_caminfo.py](https://github.com/Insper/robot22.2/blob/master/projeto/aruco/aruco_caminfo.py)

# Instruções sobre os tópicos da garra 

[Fonte: https://github.com/arnaldojr/mybot_description/](https://github.com/arnaldojr/mybot_description/)

Launch para subir os controles da garra e RViz

        roslaunch mybot_description mybot_control2.launch 

Para publicar um topico da garra:

Joint1 = braço da garra. Valores máximos:

    Garra recolhida: -1
    Garra para frente: 0
    Garra levantada: 1.5
    
    No terminal:
        rostopic pub -1 /joint1_position_controller/command std_msgs/Float64 "data: 0"
    
Joint2 = Pinça da garra.

    Pinça fechada: 0
    Pinça aberta: -1
    
    No terminal:
        rostopic pub -1 /joint2_position_controller/command std_msgs/Float64 "data: 0"
    
Visualizar arvore:

    rosrun rqt_gui rqt_gui 
    
Exemplo de codigo py:

[https://github.com/Insper/robot22.2/blob/master/ros/exemplos_222/scripts/garra_simples.py](https://github.com/Insper/robot22.2/blob/master/ros/exemplos_222/scripts/garra_simples.py)


