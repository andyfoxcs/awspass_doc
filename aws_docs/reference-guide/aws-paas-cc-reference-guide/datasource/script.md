# 脚本模式 · AWS PaaS文档中心

# 脚本模式

脚本模式是为高级开发者提供的自定义输入输出参数转换的入口。

输出示例：

> 假设场景：需要将服务端返回的数值状态转换为中文
    
    
    var $result = {
        result:{
            rows:map(result.rows, function(row, indexOfrows) {
                return{
                    USERID:row.USERID,
                    USERNAME:row.USERNAME,
                    CREATEDATE:row.CREATEDATE,
                    CLOSED:row.CLOSED,
                    ISMANAGER:convert(row.ISMANAGER) //调用自定义的转换函数
                };
            })
        },
        page:{
            total:page.total
        },
        sla:{
            inTimes:sla.inTimes,
            outTimes:sla.outTimes,
            totalTimes:sla.totalTimes
        }
    };
    
    //转换ISMANAGER为具有可读性的中文
    function convert(ISMANAGER) {
        var result;
        if ( "0" == ISMANAGER) {
            result = '否';
        } else if ("1" == ISMANAGER) {
            result = '是';
        }
        return result = result;
    }