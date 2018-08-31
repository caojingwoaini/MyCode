package com.net;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

import org.junit.Test;

public class TestSocket3 {
	@Test
	public void client() throws Exception{
		//1.创建socket对象
		Socket socket=new Socket("127.0.0.1",8989);
		//2.从本地获取一个文件发送给服务端
		OutputStream os=socket.getOutputStream();
		FileInputStream fis=new FileInputStream(new File("/Users/caojingwoaini/Desktop/1.jpg"));
		byte[] b=new byte[1024];
		int len;
		while((len=fis.read(b))!=-1) {
			os.write(b,0,len);
		}
		socket.shutdownOutput();
		//3.接收来自于服务端的消息
		InputStream is=socket.getInputStream();
		byte[] b1=new byte[1024];
		int len1;
		while((len1=is.read(b1))!=-1) {
			String str=new String(b1,0,len1);
			System.out.println(str);
		}
		//4.关闭相应的流和socket对象
		is.close();
		os.close();
		fis.close();
		socket.close();
	}
	
	@Test
	public void server() throws Exception {
		//1.创建一个ServerSocket对象
		ServerSocket ss=new ServerSocket(8989);
		//2.让客户端来连接该服务端
		Socket s=ss.accept();
		//3.将从客户端发送来的消息保存到本地
		InputStream is=s.getInputStream();
		FileOutputStream fos=new FileOutputStream(new File("/Users/caojingwoaini/Desktop/2.jpg"));
		byte[] b=new byte[1024];
		int len;
		while((len=is.read(b))!=-1) {
			fos.write(b,0,len);
		}
		System.out.println("收到来自于客户端"+s.getInetAddress().getHostAddress()+"的文件");
		//4.发送“接收成功”的信息反馈给客户端
		OutputStream os=s.getOutputStream();
		os.write("客户端发送的图片服务端已接收成功".getBytes());
		//5.关闭相应的流和socket和ServerSocket的对象
		os.close();
		fos.close();
		is.close();
		s.close();
		ss.close();
	}
	

}

