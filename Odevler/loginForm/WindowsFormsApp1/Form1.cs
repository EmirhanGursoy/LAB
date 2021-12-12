using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.OleDb;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        OleDbConnection con=new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0; Data Source=dbLogin.accdb");
        OleDbCommand cmd;
        OleDbDataReader dr;


        private void btngiris_Click(object sender, EventArgs e)
        {
            string ad = txtkullanici.Text;
            string parola = txtsifre.Text;
            cmd = new OleDbCommand();
            con.Open();
            cmd.Connection = con;
            cmd.CommandText = "SELECT *FROM Login WHERE kullanici='" + ad + "' AND sifre='" + parola + "'";
            dr = cmd.ExecuteReader();
            if (dr.Read())
            {
                label3.Text = "Hoş Geldin emirhan";
            }
            else
            {
                label3.Text = "Kullanıcı adı veya şifre hatalı!";
            }
            
            con.Close();

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                txtsifre.PasswordChar = '*';
            }
            else
            {
                txtsifre.PasswordChar = '\0';
            }
        }
    }
}
