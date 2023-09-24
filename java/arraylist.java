import java.util.ArrayList;
import java.util.Arrays;

enum FolderType {
    CLASSIFICATION("Classification"),
    OBJECT_DETECTION("Object Detection"),
    SEGMENTATION("Segmentation"),
    NON_ANNOTATED("Non-Annotated"),
    ANOMALY_DETECTION("Anomaly Detection");

    private final String name;

    private FolderType(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

}


class A {
    static public void main(String args[]){
        var ft = FolderType.CLASSIFICATION;
        var allowCrop = new ArrayList<>(Arrays.asList(FolderType.ANOMALY_DETECTION, FolderType.CLASSIFICATION ));
        if (! allowCrop.contains(ft)) {
            System.out.println("No");
        } 
        
        System.out.println(allowCrop);
    }
}