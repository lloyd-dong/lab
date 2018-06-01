package com.company;

/**
 * Created by bodong on 27/10/2017.
 */
public class CMI {
    public Builder toBuilder(){return new Builder();}
    final class Builder{
        Builder(){
            System.out.println("in CDM");
        }
    }
    static public void main(String[] argc){
        CDMIndoor c = new CDMIndoor();
        c.toBuider();
    }
}
class CDMIndoor extends CMI{
    public Builder toBuider(){return new Builder();}
    final class Builder{
        Builder(){
            System.out.println("in CDMIndoor");
        }
    }
}