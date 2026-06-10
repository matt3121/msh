using System;
using System.ComponentModel;
using System.Data;
using System.Security.Cryptography.X509Certificates;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("test");
        Console.ReadKey(); 
        

        
    }

}

public class token
{
    
    public static readonly string TT_INT = "INT";
    public static readonly string TT_PLUS = "PLUS";
    public static readonly string TT_MINUS = "MINUS";
    public static readonly  string TT_FLOAT = "FLOAT";
    public static readonly string TT_MUL = "MUL";
    public static readonly string TT_DIV = "DIV";
    public static readonly string TT_LPAREN = "LPAREN";
    public static readonly string TT_RPAREN = "RPAREN";
    public string type_;
    public int value;

    public token(string type_, int value)
    {
        this.type_ = type_;
        this.value = value;
    }
    public override string ToString()
    {
        if (!string.IsNullOrEmpty(this.type_))
        {
            return $"Token(type_={this.type_}, value={this.value})";
        }
        
        
            return $"Token(type_={this.type_}";
    
       
    }

    public void ignore()
    {
        
    }
}

public class Lexer
{
    private string text;
    public int currentPos;
    public string current_char;

    public Lexer(string text)
    {
        this.text = text;a
        this.currentPos = -1;
        this.current_char = null;
    }
}