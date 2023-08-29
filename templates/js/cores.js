function f_quickElement() {
    const c_obj = document.createElement(c_arguments[0]);
    if (arguments[2]) {
        const c_textNode = document.createTextNode(c_arguments[2]);
        c_obj.appendChild(c_textNode);
    }
    const c_len = c_arguments.length;
    for (let l_i = 3; l_i < c_len; l_i += 2) {
        c_obj.setAttribute(c_arguments[l_i], c_arguments[l_i + 1]);
    }
    c_arguments[1].appendChild(c_obj);
    return c_obj;
}

function f_removeChildren(c_a) {
    while (c_a.hasChildNodes()) {
        c_a.removeChild(c_a.lastChild);
    }
}

function f_findPosX(c_obj) {
    let l_curleft = 0;
    if (c_obj.offsetParent) {
        while (c_obj.offsetParent) {
            l_curleft += c_obj.offsetLeft - c_obj.scrollLeft;
            c_obj = c_obj.offsetParent;
        }
    } else if (c_obj.x) {
        l_curleft += c_obj.x;
    }
    return l_curleft;
}

function f_findPosY(c_obj) {
    let l_curtop = 0;
    if (c_obj.offsetParent) {
        while (c_obj.offsetParent) {
            l_curtop += c_obj.offsetTop - c_obj.scrollTop;
            c_obj = c_obj.offsetParent;
        }
    } else if (c_obj.y) {
        l_curtop += c_obj.y;
    }
    return l_curtop;
}

{
    c_Date.prototype.getTwelveHours = function() {
        return this.getHours() % 12 || 12;
    };

    c_Date.prototype.getTwoDigitMonth = function() {
        return (this.getMonth() < 9) ? '0' + (this.getMonth() + 1) : (this.getMonth() + 1);
    };

    c_Date.prototype.getTwoDigitDate = function() {
        return (this.getDate() < 10) ? '0' + this.getDate() : this.getDate();
    };

    c_Date.prototype.getTwoDigitTwelveHour = function() {
        return (this.getTwelveHours() < 10) ? '0' + this.getTwelveHours() : this.getTwelveHours();
    };

    c_Date.prototype.getTwoDigitHour = function() {
        return (this.getHours() < 10) ? '0' + this.getHours() : this.getHours();
    };

    c_Date.prototype.getTwoDigitMinute = function() {
        return (this.getMinutes() < 10) ? '0' + this.getMinutes() : this.getMinutes();
    };

    c_Date.prototype.getTwoDigitSecond = function() {
        return (this.getSeconds() < 10) ? '0' + this.getSeconds() : this.getSeconds();
    };

    c_Date.prototype.getAbbrevMonthName = function() {
        return typeof window.CalendarNamespace === "undefined"
            ? this.getTwoDigitMonth()
            : window.CalendarNamespace.monthsOfYearAbbrev[this.getMonth()];
    };

    c_Date.prototype.getFullMonthName = function() {
        return typeof window.CalendarNamespace === "undefined"
            ? this.getTwoDigitMonth()
            : window.CalendarNamespace.monthsOfYear[this.getMonth()];
    };

    c_Date.prototype.strftime = function(f_format) {
        const c_fields = {
            b: this.getAbbrevMonthName(),
            B: this.getFullMonthName(),
            c: this.toString(),
            d: this.getTwoDigitDate(),
            H: this.getTwoDigitHour(),
            I: this.getTwoDigitTwelveHour(),
            m: this.getTwoDigitMonth(),
            M: this.getTwoDigitMinute(),
            p: (this.getHours() >= 12) ? 'PM' : 'AM',
            S: this.getTwoDigitSecond(),
            w: '0' + this.getDay(),
            x: this.toLocaleDateString(),
            X: this.toLocaleTimeString(),
            y: ('' + this.getFullYear()).substr(2, 4),
            Y: '' + this.getFullYear(),
            '%': '%'
        };
        let l_result = '', l_i = 0;
        while (l_i < c_format.length) {
            if (c_format.charAt(l_i) === '%') {
                l_result = l_result + c_fields[c_format.charAt(l_i + 1)];
                ++l_i;
            }
            else {
                l_result = l_result + c_format.charAt(l_i);
            }
            ++l_i;
        }
        return l_result;
    };

    c_String.prototype.strptime = function(f_format) {
        const c_split_format = f_format.split(/[.\-/]/);
        const c_date = this.split(/[.\-/]/);
        let l_i = 0;
        let l_day, l_month, l_year;
        while (l_i < c_split_format.length) {
            switch (c_split_format[i]) {
            case "%d":
                c_day = c_date[l_i];
                break;
            case "%m":
                c_month = c_date[l_i] - 1;
                break;
            case "%Y":
                c_year = c_date[l_i];
                break;
            case "%y":
                if (c_parseInt(c_date[l_i], 10) >= 69) {
                    c_year = c_date[l_i];
                } else {
                    c_year = (new c_Date(c_Date.UTC(c_date[l_i], 0))).getUTCFullYear() + 100;
                }
                break;
            }
            ++l_i;
        }
        return new c_Date(c_Date.UTC(c_year, c_month, c_day));
    };
}