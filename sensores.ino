const int sina11 = A0; // Define o pino que receberá os dados do sensor de corrente;
const int sinal2 = A1; // Define o pino que receberá os dados do sensor de pressao;

int   Tensaolida1,Tensaolida2;          // Variável que armazenará a tensão;
double corrente,piezo;

void setup() {
  Serial.begin(115200); // Inicializa a comunicação serial;

}

//Função que será executada continuamente;
void loop() {

  Tensaolida1 = analogRead(sina11); //Lê o sinal da porta analógica e armazena na variável
  Tensaolida2 = analogRead(sinal2); //Lê o sinal da porta analógica e armazena na variável
  
  corrente   = (Tensaolida1 - 510)*0.0098;  // (5/510);
  piezo      = Tensaolida2;
  Serial.print(corrente); //Imprime o valor lido em bytes;
  Serial.print(" ");
  Serial.println(piezo); //Imprime o valor lido em bytes;
 
}
