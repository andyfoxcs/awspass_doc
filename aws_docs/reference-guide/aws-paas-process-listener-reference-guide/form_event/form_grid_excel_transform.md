# FORM_GRID_EXCEL_TRANSFORM | AWS 流程事件开发参考指南

## FORM_GRID_EXCEL_TRANSFORM

### 表单子表Excle转换处理

项 | 说明  
---|---  
抽象类 | ExcelTransformListener  
返回值 | 无  
异常 | -如抛出异常时，异常被包装成结果返回，后继执行被中断  
  
### 常见触发场景

**1.上传或下载子表Excel文件时**

![](https://docs.awspaas.com/reference-guide/aws-paas-process-listener-reference-guide/form_event/9.png)

### 开发示例

**时间点常量说明**

常量 | 描述  
---|---  
ListenerConst.FORM_EXCEL_TIMESTATE_IMPORT_BEFORE | 导入前的时间点  
ListenerConst.FORM_EXCEL_TIMESTATE_IMPORT_AFTER | 导入后的时间点，整体导入后会触发保存后事件  
ListenerConst.FORM_EXCEL_TIMESTATE_DOWNLOADTPL_BEFOR | 下载模版文件之前的时间点  
ListenerConst.FORM_EXCEL_TIMESTATE_EXPORT_AFTER | 导出后（生成文件之前）的时间点  
  
**注意，如果Workbook对象在接口实现的过程中做了修改，接口调用方并不会读取修改过的内容**
    
    
    package com.actionsoft.apps.poc.form.event;
    
    import org.apache.poi.hssf.usermodel.HSSFWorkbook;
    import org.apache.poi.ss.usermodel.Workbook;
    import org.apache.poi.xssf.streaming.SXSSFWorkbook;
    
    import com.actionsoft.bpms.bpmn.engine.core.delegate.ProcessExecutionContext;
    import com.actionsoft.bpms.bpmn.engine.listener.ExcelTransformListener;
    import com.actionsoft.bpms.bpmn.engine.listener.ListenerConst;
    
    public class TestFormExcelTransform extends ExcelTransformListener {
    
        public String getDescription() {
            return "表单中，下载、上传Excel后处理Excel文件的事件测试";
        }
    
        public String getProvider() {
            return "Actionsoft";
        }
    
        public String getVersion() {
            return "1.0";
        }
    
        @Override
        public Workbook fixExcel(ProcessExecutionContext ctx, Workbook wb) {
            //参数获取
            //注意：除特殊说明外，下列参数仅在该事件中场景有效
            ctx.getUserContext();// 用户上下文对象
            // 时间点的常量见上表
            String timeState = ctx.getParameterOfString(ListenerConst.FORM_EVENT_PARAM_EXCEL_TIMESTATE);// 通过该值判断当前事件所处的时间点
            // 判断方式
            if (ListenerConst.FORM_EXCEL_TIMESTATE_IMPORT_BEFORE.equals(timeState)) {
                // ...
            }
    
            //wb对象可以构造为HSSFWorkbook或者SXSSFWorkbook
            if (wb instanceof HSSFWorkbook) {
                // 解析Excel（xls格式）
            }
            if (wb instanceof SXSSFWorkbook) {
                // 解析Excel（xlsx格式）
            }
    
            // 如果想要阻止下载或者上传的后续操作，可以return null;
    
            return wb;//注意，即使对该对象进行修改，上层程序也不会读取新的数据。
        }
    
    }