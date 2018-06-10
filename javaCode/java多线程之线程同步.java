package com.fanyanwei;

public class ThreadDemo implements Runnable{
	private int piao=5;
	
	public void run() {
		while(true) {
			//添加同步代码块来加上资源锁
			synchronized (this) {
				if(piao<=0) {
					break;
				}
				try {
					Thread.sleep(2000);
				}catch(Exception e) {
					System.out.println(e);
				}
				System.out.println(Thread.currentThread()+">>>>还剩余票数:"+piao--);
			}
		}
	}
	
	public static void main(String[] args) {
		ThreadDemo thread1=new ThreadDemo();
		Thread t1=new Thread(thread1);
		Thread t2=new Thread(thread1);
		Thread t3=new Thread(thread1);
		t1.setPriority(Thread.MIN_PRIORITY);
		t2.setPriority(Thread.NORM_PRIORITY);
		t3.setPriority(Thread.MAX_PRIORITY);
		t1.start();
		t2.start();
		t3.start();
	}
}

/*
返回结果:
	Thread[Thread-0,1,main]>>>>还剩余票数:5
	Thread[Thread-0,1,main]>>>>还剩余票数:4
	Thread[Thread-0,1,main]>>>>还剩余票数:3
	Thread[Thread-0,1,main]>>>>还剩余票数:2
	Thread[Thread-0,1,main]>>>>还剩余票数:1
*/