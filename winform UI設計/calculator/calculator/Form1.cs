using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool isResult = true;
        double prevNumber = 0;
        string prevOperator = "=";
        const int digit = 5;
        Form2 form2;

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "0";
            form2 = new Form2();
        }
        private void Button_NumberClick(object sender, EventArgs e)
        {   
            Button clickedBtn = (Button)sender;

            if (isResult)
            {
                label1.Text = (clickedBtn.Text == ".") ? "0." : clickedBtn.Text;
                isResult = false;
                return;
            }

            if (clickedBtn.Text == ".")
            {
                label1.Text += clickedBtn.Text;
                return;
            }

            if(label1.Text != "0")
            {
                label1.Text += clickedBtn.Text;
            }
            else
            {
                label1.Text = clickedBtn.Text;
            }   
        }

        private void Button_OperatorClick(object sender, EventArgs e)
        {
            Button clickedButton = (Button)sender;
            string log = "";
            if (label1.Text == "")
            {
                prevOperator = clickedButton.Text;
                return;
            }
            double curNumber = Double.Parse(label1.Text);
            log += prevNumber.ToString() + prevOperator + curNumber.ToString() + " = ";
            if (prevOperator == "+") curNumber = prevNumber + curNumber;
            else if (prevOperator == "-") curNumber = prevNumber - curNumber;
            else if (prevOperator == "*") curNumber = prevNumber * curNumber;
            else if (prevOperator == "/")
            {
                if (curNumber == 0)
                {
                    MessageBox.Show("不可除以 0", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }
                curNumber = prevNumber / curNumber;
            }
            log += curNumber.ToString();
            if(prevOperator != "=") form2.writeLog(log);

            prevNumber = curNumber;
            label1.Text = "";
            if (clickedButton.Text == "=")
            {
                curNumber = Math.Round(curNumber, digit, MidpointRounding.AwayFromZero);
                label1.Text = curNumber.ToString();
                isResult = true;
            }
            else
            {
                isResult = false;
            }
            prevOperator = clickedButton.Text;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            label1.Text = "0";
            prevNumber = 0;
            prevOperator = "=";
            isResult = true;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length > 1)
            {
                label1.Text = label1.Text.Substring(0, label1.Text.Length - 1);
            }
            else
            {
                label1.Text = "0";
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            form2.Show();
        }
    }
}
