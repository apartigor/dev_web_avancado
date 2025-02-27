class Program
{
    static void Main(string[] args)
    {
        Carro carro = new Carro("Fusca", 1980);
        carro.ExibirDetalhes();
    }
}


class Carro
{

    public string Modelo { get; set; }
    public int Ano { get; set; }
    public Carro(string modelo, int ano)
    {
        Modelo = modelo;
        Ano = ano;
    }

    public void ExibirDetalhes()
    {
        Console.WriteLine($"Modelo: {Modelo}, Ano: {Ano} ");
    }
}

