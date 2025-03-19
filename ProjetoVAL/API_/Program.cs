using API.Models;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();


List<Agente> agentes = new List<Agente>();

agentes.Add(new Agente (){
    Nome = "Jett",
    Nacionalidade = "Coreia do Sul"
});
agentes.Add(new Agente (){
    Nome = "Phoenix",
    Nacionalidade = "Inglaterra"
});




app.MapGet("/", () => "Agentes do Valorant");

app.MapGet("/lista_agentes", () =>
{
    return Results.Ok(agentes);
});

app.MapPost("/criar_agente", () => {
    
});

app.Run();
