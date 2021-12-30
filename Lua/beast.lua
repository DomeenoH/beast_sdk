-- utf8转字符
local d = tonumber("591a", 16)
print(d)

local m = tonumber("7c73", 16)
print(m)

local n = tonumber("8bfa", 16)
print(n)

local a = utf8.char(d, m, n)
print(a)

-- 取utf8编码
local code = ""
for p, c in utf8.codes("多米诺") do
    print(c)
    code = code .. c .. ","
end
print(code)

-- 16进制转10进制
function hex_tonumber(hex_str)
    local num = tonumber(hex_str, 16)
    return num
end

-- 10进制转16进制
str = "12345"
print(string.format("%#x", str))

-- 运算，取商和余数
print(7 // 4)
print(math.fmod(7, 4))


---------------------------------------------------
-- 加密第一步，字符转16进制unicode的4位数字
function str2hex(str)
    local ret = ""
    for p, c in utf8.codes(str) do
        local charHexStr = string.sub(string.format("%#x",c),3,-1)
        if string.len(charHexStr) == 3 then
            charHexStr = "0" .. charHexStr
        elseif string.len(charHexStr) == 2 then
            charHexStr = "00" .. charHexStr
        end
        ret = ret..charHexStr
    end
    return ret
end


-- 加密第二步，对字符串进行二次加密
function aowua(str)

end


-- 解密第一步，将兽语转换为16进制unicode字符串



-- 解密第二步，将unicode字符串恢复为文本
function hex2str(str)
    local ret = ""
    local i = 1
    while(i<=string.len(str))
    do
        charStr = utf8.char(tonumber(string.sub(str, i , i+3),16))
        ret = ret..charStr
        i = i+4
    end
	return(ret)
end
-----------------------------------------------------
print("591a7c738bfa003100320033")
print(hex2str("591a7c738bfa003100320033"))