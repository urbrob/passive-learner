package passive_learner.urbrob.github.com.app

import android.content.Context
import java.io.File
import java.io.FileInputStream

class FileManager(private val context: MainActivity) {

    private fun copyToLocal(fileName: String, source: File) {
        source.inputStream().use { input ->
            context.openFileOutput(fileName, Context.MODE_PRIVATE).use { output ->
                input.copyTo(output)
            }
        }
    }

    fun saveToLocalFile(fileName: String, content: String) {
        context.openFileOutput(fileName, Context.MODE_PRIVATE).use {
            it.write(content.toByteArray())
        }
    }

    fun deleteLocalFile(fileName: String) {
        context.deleteFile(fileName)
    }

    fun setActualPlan(fileName: String): FileInputStream {
        val pref = context.getPreferences(Context.MODE_PRIVATE)
        with(pref.edit()) {
            putString("actualPlan", fileName)
            apply()
        }
        return context.openFileInput(fileName)
    }

    fun getActualPlan(): FileInputStream {
        val fname = context.getPreferences(Context.MODE_PRIVATE).getString("actualPlan", null)
        return context.openFileInput(fname)
    }

    fun importExternalFile(path: String, newFileName: String? = null, makeActual: Boolean = false): FileInputStream? {
        val fname: String
        val file = File(path)
        fname = if (newFileName.isNullOrBlank()) {
            file.name
        } else {
            newFileName
        }
        copyToLocal(fname, file)
        if (makeActual) {
            return setActualPlan(fname)
        }
        return null
    }
}