package jsqlite;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Utils {
	
	static Scanner teclado = new Scanner(System.in);
	
	public static Connection conectar() {
		String URL_SERVIDOR = "jdbc:sqlite:src/jsqlite/jsqlite3.geek";
		
		try {
			Connection conn = DriverManager.getConnection(URL_SERVIDOR);
			
			String TABLE = "CREATE TABLE IF NOT EXISTS produtos("
					+ "id INTEGER PRIMARY KEY AUTOINCREMENT,"
					+ "nome TEXT NOT NULL,"
					+ "preco REAL NOT NULL,"
					+ "estoque INTEGER NOT NULL);";
			
			Statement stmt = conn.createStatement();
			stmt.executeUpdate(TABLE);
			
			return conn;
		}catch(Exception e) {
			e.printStackTrace();
			System.out.println("Não foi possível conectar ao SQLite: " + e);
			return null;
		}
	}
	
	public static void desconectar(Connection conn) {
		try {
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public static void listar() {
		String BUSCAR_TODOS = "SELECT * FROM produtos";
		
		try {
			Connection conn = conectar();
			PreparedStatement produtos = conn.prepareStatement(BUSCAR_TODOS);
			ResultSet res = produtos.executeQuery();
			
			while(res.next()) {
				System.out.println("------Produto-----");
				System.out.println("ID: " + res.getInt(1));
				System.out.println("Produto: " + res.getString(2));
				System.out.println("Preço: " + res.getFloat(3));
				System.out.println("Estoque: " + res.getInt(4));
				System.out.println("-------------------------");
			}
			produtos.close();
			desconectar(conn);
		}catch(Exception e) {
			e.printStackTrace();
			System.err.println("Erro ao buscar todos os produtos.");
			System.exit(-42);
		}
	}
	
	public static void inserir() {
		System.out.println("Informe o nome do produto: ");
		String nome = teclado.nextLine();
		
		System.out.println("Informe o preço do produto: ");
		float preco = teclado.nextFloat();
		
		System.out.println("Informe a quantidade em estoque: ");
		int estoque = teclado.nextInt();
		
		String INSERIR = "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)";
		
		try {
			Connection conn = conectar();
			PreparedStatement salvar = conn.prepareStatement(INSERIR);
			
			salvar.setString(1, nome);
			salvar.setFloat(2,  preco);
			salvar.setInt(3, estoque);
			
			int res = salvar.executeUpdate();
			
			if(res > 0) {
				System.out.println("O produto " + nome + " foi inserido com sucesso.");
			}else {
				System.out.println("Não foi possível inserir o produto.");
			}
			salvar.close();
			desconectar(conn);
		}catch(Exception e) {
			e.printStackTrace();
			System.err.println("Erro salvando dados.");
		}
	}
	
	public static void atualizar() {
		System.out.println("Informe o código do produto: ");
		int id = Integer.parseInt(teclado.nextLine());
		
		try {
			Connection conn = conectar();
			
			System.out.println("Informe o nome do produto: ");
			String nome = teclado.nextLine();
			
			System.out.println("Informe o preço do produto: ");
			float preco = teclado.nextFloat();
			
			System.out.println("Informe a quantidade em estoque: ");
			int estoque = teclado.nextInt();
			
			String ATUALIZAR = "UPDATE produtos SET nome=?, preco=?, estoque=? WHERE id=?";
			
			PreparedStatement upd = conn.prepareStatement(ATUALIZAR);
			
			upd.setString(1, nome);
			upd.setFloat(2, preco);
			upd.setInt(3, estoque);
			upd.setInt(4, id);
			
			int res = upd.executeUpdate();
			
			if(res > 0) {
				System.out.println("O produto " + nome + " foi atualizado com sucesso.");
			}else {
				System.out.println("Não foi possível atualizar o produto com id " + id);
			}
			upd.close();
			desconectar(conn);
		}catch(Exception e) {
			e.printStackTrace();
			System.err.println("Não foi possível atualizar o produto com id "  + id);
		}
	}
	
	public static void deletar() {
		String DELETAR = "DELETE FROM produtos WHERE id=?";
		
		System.out.println("Informe o código do produto: ");
		int id = Integer.parseInt(teclado.nextLine());
		
		try {
			Connection conn = conectar();
			
			PreparedStatement del = conn.prepareStatement(DELETAR);
			del.setInt(1, id);
			
			int res = del.executeUpdate();
			
			if(res > 0) {
				System.out.println("O produto foi deletado com sucesso.");
			}else {
				System.out.println("Não foi possível deletar o produto com id " + id);
			}
			del.close();
			desconectar(conn);
		}catch(Exception e) {
			e.printStackTrace();
			System.err.println("Erro ao deletar produto.");
		}
	}
	
	public static void menu() {
		System.out.println("==================Gerenciamento de Produtos===============");
		System.out.println("Selecione uma opção: ");
		System.out.println("1 - Listar produtos.");
		System.out.println("2 - Inserir produtos.");
		System.out.println("3 - Atualizar produtos.");
		System.out.println("4 - Deletar produtos.");
		
		int opcao = Integer.parseInt(teclado.nextLine());
		if(opcao == 1) {
			listar();
		}else if(opcao == 2) {
			inserir();
		}else if(opcao == 3) {
			atualizar();
		}else if(opcao == 4) {
			deletar();
		}else {
			System.out.println("Opção inválida.");
		}
	}
}
